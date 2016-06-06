# -*- coding: utf-8 -*-
##############################################################################
#  COMPANY: BORN
#  AUTHOR: KIWI
#  EMAIL: arborous@gmail.com
#  VERSION : 1.0   NEW  2014/07/21
#  UPDATE : NONE
#  Copyright (C) 2011-2014 www.wevip.com All Rights Reserved
##############################################################################

import os
import time
import json
import logging
import random
import string
from datetime import datetime, timedelta
import werkzeug.utils
import openerp
from mako import exceptions
from openerp.http import request
from openerp import SUPERUSER_ID
from openerp.addons.web import http
from mako.lookup import TemplateLookup
from mako.template import Template
from openerp.addons.tl_weixin.tools.client import Client

import xmlrpclib
import time
import hashlib
import openerp
import string
from openerp import SUPERUSER_ID
import random

try:
    import hashlib

    md5_constructor = hashlib.md5
    md5_hmac = md5_constructor
    sha_constructor = hashlib.sha1
    sha_hmac = sha_constructor
except ImportError:
    import md5

    md5_constructor = md5.new
    md5_hmac = md5
    import sha

    sha_constructor = sha.new
    sha_hmac = sha
md5 = md5_constructor
_logger = logging.getLogger(__name__)

# MAKO
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DEFAULT_THEME = "app"
path = os.path.join(BASE_DIR, "static", DEFAULT_THEME)
tmp_path = os.path.join(path, "tmp")
lookup = TemplateLookup(directories=[path], output_encoding='utf-8', module_directory=tmp_path)

BASE_LOTTERY_PATH = os.path.join(BASE_DIR, "static", 'games')


# 获取模版信息
def get_template(templatename, **kwargs):
    try:
        template = lookup.get_template(templatename)
        return template.render(**kwargs)
    except:
        return exceptions.html_error_template().render()


class Lottery(http.Controller):
    # 初始化
    @http.route(['/<string:db>/lottery'], type='http', auth="none", csrf=False)
    def lottery(self, db=None, **post):

        # 验证微信
        agent = request.httprequest.environ.get('HTTP_USER_AGENT', '').lower()
        weixin_angent = agent.find('micromessenger')
        key = post.get('key', False)
        code = post.get('code', False)
        state = post.get('state', False)
        if code:
            key = state

        if not db:
            errmsg = u'参数错误'
            return get_template('error.html', errmsg=errmsg)
        request.session.db = db

        activity_obj = request.env['born.activity']
        domain = [('born_uuid', '=', key), ('status', 'in', ('processing', 'finish'))]
        activity = activity_obj.sudo().search(domain, limit=1)
        if not activity:
            errmsg = u'活动未开始或活动不存在'
            return get_template('error.html', errmsg=errmsg)

        if weixin_angent > 0:
            # 微信鉴权
            if code and activity.active_tpl_id.app_id:
                user_obj = request.env['tl.weixin.users']
                client = Client(request.registry, request.cr, SUPERUSER_ID, activity.active_tpl_id.app_id, False)
                user=user_obj.sudo().create_or_update_user_by_code_not_subscribe(activity.active_tpl_id.app_id.id,code)
                request.session.wx_uid = user.id

            else:
                return werkzeug.utils.redirect(activity.weixin_url)

        url = '/%s/activity?key=%s' % (db, key)
        request.session.aid = activity.id
        return werkzeug.utils.redirect(url)

    # 活动
    @http.route(['/<string:db>/activity'], type='http', auth="none", csrf=False)
    def activity(self, db=None, **post):
        data = {}

        key = post.get('key', False)
        # 查看活动信息
        if not db or not key:
            errmsg = u'参数错误'
            return get_template('error.html', errmsg=errmsg)

        request.session.db = db
        activity_obj = request.env['born.activity']
        domain = [('born_uuid', '=', key), ('status', 'in', ('processing', 'finish'))]
        activity = activity_obj.sudo().search(domain, limit=1)
        if not activity:
            errmsg = u'活动未开始或活动不存在'
            return get_template('error.html', errmsg=errmsg)

        # 验证是否在微信中打开
        agent = request.httprequest.environ.get('HTTP_USER_AGENT', '').lower()
        weixin_angent = agent.find('micromessenger')
        if weixin_angent > 0:
            # 没有授权
            if not request.session.wx_uid:
                return werkzeug.utils.redirect(activity.weixin_url)

        return get_template('index.html', activity=activity)

    # 游戏
    @http.route(['/<string:db>/activity_game/<string:key>'], type='http', auth="none", csrf=False)
    def game(self, db=None, key=None, **post):

        if not db or not key:
            errmsg = u'参数错误'
            return get_template('error.html', errmsg=errmsg)

        request.session.db = db
        # 查找活动

        pid = request.session.pid
        wx_uid = request.session.wx_uid
        aid = request.session.aid

        activity_obj = request.env['born.activity']
        domain = [('born_uuid', '=', key), ('status', 'in', ('processing', 'finish'))]
        activity = activity_obj.sudo().search(domain, limit=1)
        if not activity or aid != activity.id:
            errmsg = u'活动未开始或活动不存在'
            return get_template('error.html', errmsg=errmsg)

        if not activity.active_tpl_id.game_id:
            errmsg = u'该活动不能参加游戏'
            return get_template('error.html', errmsg=errmsg)

        # 验证是否在微信中打开
        agent = request.httprequest.environ.get('HTTP_USER_AGENT', '').lower()
        weixin_angent = agent.find('micromessenger')
        if weixin_angent > 0:
            # 没有授权
            if not request.session.wx_uid:
                return werkzeug.utils.redirect(activity.weixin_url)

        # 需要注册
        if not request.session.pid and not request.session.wx_uid:
            request.session.redirect_url = '/%s/activity_game/%s' % (db,key)
            return get_template('signup.html')

        # 搜索该用户是否已经参加了游戏
        result_obj = request.env['born.activity.result']
        domain = [('activity_id', '=', aid)]
        if pid:
            domain += [('partner_id', '=', pid)]
        if wx_uid:
            domain += [('weixin_user_id', '=', wx_uid)]
        qty = result_obj.sudo().search_count(domain)

        remain_qty = activity.game_chance - qty

        domain=[('activity_id', '=', aid),('activity_gift_id', '!=', False)]
        join_price_ids = result_obj.sudo().search(domain,limit=10)
        game={
            'game_name':activity.game_id.name,
            'remain_qty':remain_qty,
            'company_name':activity.active_tpl_id.app_id.name,
            'subscribe_url': activity.active_tpl_id.app_id.subscribe_url,
            'game_chance':activity.game_chance,
            'join_price_ids':join_price_ids,
            'gift_ids':activity.gift_ids,
            'game_description':activity.game_id.description,
            'born_uuid':activity.born_uuid,
            'account_url':'/%s/%s/account' % (db,activity.active_tpl_id.app_id.appid),
        }

        #绑定微信
        cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
        client_obj = Client(pool, cr, uid=openerp.SUPERUSER_ID, app=activity.active_tpl_id.app_id, open_app=False)
        jsapi_ticket = client_obj.jsapi_ticket()
        data = {
            'timestamp': int(time.time()),
            'jsapi_ticket': jsapi_ticket,
            'url': '%s/%s/activity_game/%s' % (openerp.tools.config['localhost_server_url'],db, key),
            'nonceStr': ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15)),
        }
        data_str = '&'.join(['%s=%s' % (key.lower(), data[key]) for key in sorted(data)])
        data['signature'] = hashlib.sha1(data_str).hexdigest()
        data['appId'] = activity.active_tpl_id.app_id.appid


        game_path = activity.active_tpl_id.game_id.path
        tpl = Template(filename=BASE_LOTTERY_PATH + game_path)
        return tpl.render(game=game,data=data)

    # 会员卡绑定获取短信验证码
    @http.route(['/activity/get_code',
                 '/activity/get_code?phone=<string:phone>',
                 ], type='http', auth="none", methods=['POST'], csrf=False)
    def activity_get_code(self, phone=None, **kw):

        if not request.session.db:
            return json.dumps({'errcode': 1, 'errmsg': u'错误'})

        aid = request.session.aid
        if phone and aid:
            activity_obj = request.env['born.activity']
            activity = activity_obj.sudo().browse(int(aid))
            if activity:
                captcha = random.randint(100000, 999999)
                args = {'param2': captcha, 'param1': activity.app_id.company_id.name, 'param3': 30}
                ret = sms_obj.sudo().send_message_for_call(phone, '91550899', args, 1, captcha)
                return json.dumps({'errcode': 0, 'errmsg': u'短信已发送'})
        return json.dumps({'errcode': 1, 'errmsg': u'发送短信失败'})

    # 会员卡绑定验证验证码是否正确
    @http.route(['/activity/check_code',
                 '/activity/check_code?phone=<string:phone>&code=<string:code>',
                 ], type='http', auth="none", methods=['POST'], csrf=False)
    def activity_check_code(self, phone=None, code=None, **kw):

        if not request.session.db:
            return json.dumps({'errcode': 1, 'errmsg': u'错误'})

        aid = request.session.aid
        if phone and code and aid:
            sms_obj = request.env['born.sms']
            domain = [('template_id', '=', '91550899'), ('phone', '=', phone), ('security_code', '=', code),
                      ('state', '=', 'send')]
            sms = sms_obj.sudo().search(domain, limit=1)

            if not sms:
                result = {'errcode': 1, 'errmsg': u'验证码错误'}
                return json.dumps(result)
            else:
                # 登记用户信息
                activity_obj = request.env['born.activity']
                activity = activity_obj.sudo().browse(int(aid))

                val_part = {
                    'mobile': phone,
                    'name': phone,
                    'is_lottery': True,
                    'activity_id': activity.id,
                }
                partner = activity_obj.sudo().create(val_part)
                request.session.pid = partner.id

                return json.dumps({'errcode': 0, 'errmsg': u''})
        return json.dumps({'errcode': 1, 'errmsg': u'验证码错误', 'data': {}})

    # 生成游戏奖品
    @http.route(['/activity_game_gift/<string:key>'], type='http', auth="none", csrf=False)
    def activity_game_gift(self, db=None, key=None, **post):

        if not request.session.db:
            return json.dumps({'errcode': 1, 'errmsg': u'错误'})

        pid = request.session.pid
        wx_uid = request.session.wx_uid
        aid = request.session.aid
        if (not wx_uid and not pid) or not aid:
            return json.dumps({'errcode': 1, 'errmsg': u'您不能参加抽奖', 'data': {}})

        activity_obj = request.env['born.activity']
        activity = activity_obj.sudo().browse(int(aid))
        if activity.id != aid:
            return json.dumps({'errcode': 1, 'errmsg': u'活动参数错误', 'data': {}})

        # 如果已经参与则不能
        result_obj = request.env['born.activity.result']
        domain = [('activity_id', '=', aid)]
        if pid:
            domain += [('partner_id', '=', pid)]
        if wx_uid:
            domain += [('weixin_user_id', '=', wx_uid)]
        count = result_obj.sudo().search_count(domain)

        #查看是否中奖过了
        domain+=[('activity_gift_id', '!=', False)]
        gift_count = result_obj.sudo().search_count(domain)

        if count >= activity.game_chance:
            return json.dumps({'errcode': 1, 'errmsg': u'很遗憾您没有抽奖机会了', 'data': {}})

        game_chance= activity.game_chance-count

        vals = {
            'activity_id': aid,
            'partner_id': pid,
            'weixin_user_id': wx_uid,

        }

        # 获取游戏的奖项
        game_chance=game_chance - 1
        gift_obj = request.env['born.activity.gift']
        domain = [('activity_id', '=', aid), ('probability', '>', 0)]
        gifts = gift_obj.sudo().search(domain)
        user_obj = request.env['tl.weixin.users']
        wx_uer = user_obj.sudo().browse(int(request.session.wx_uid))
        #if gifts:
        if gifts and gift_count <= 0:
            l = len(gifts)
            ids = [x.id for x in gifts]
            gid = random.choice(ids)
            gift = gift_obj.sudo().browse(int(gid))

            if gift.remain_qty > 0 and gift.probability > 0:
                probability = gift.probability
                if probability < 1:
                    str_probability = str(probability)
                    l = len(str_probability) - 2
                    max_number = int('1' + '0' * l)
                    rand_number = random.randint(1, max_number)
                    point = int(probability * max_number)

                    if rand_number <= point:
                        vals['activity_gift_id'] = gift.id
                        _logger.info(u'随机获取一个奖项,奖品为:%s' % (gift.gift_id.name))
                else:
                    vals['activity_gift_id'] = gift.id

        price = result_obj.sudo().create(vals)
        if price.activity_gift_id:
            data = {
                'level': price.activity_gift_id.level,
                'name': u'您获得的奖品为:%s' % (price.activity_gift_id.gift_id.name),
                'cardExt':price.card_ext,
                'cardId': price.activity_gift_id.gift_id.wxcard_id.wxcard_id,
                'game_chance':game_chance
            }

            _logger.info(data)

            return json.dumps({'errcode': 0, 'errmsg': u'恭喜您中奖了', 'data': data})
        return json.dumps({'errcode': 0, 'errmsg': u'很遗憾没有中奖', 'data': {'game_chance':game_chance,'level': 0, 'name': ''}})


    # 个人中心
    @http.route(['/<string:db>/<string:app_id>/account'], type='http', auth="none", csrf=False)
    def user_center(self, db=None,app_id=None, **post):

        code = post.get('code', False)
        obj_app = request.env['tl.weixin.app']
        app = obj_app.sudo().search([('appid', '=', app_id)], limit=1)
        if not app:
            errmsg = u'未授权访问'
            return get_template('error.html', errmsg=errmsg)

        agent = request.httprequest.environ.get('HTTP_USER_AGENT', '').lower()
        weixin_angent = agent.find('micromessenger')

        user_info={}

        if weixin_angent > 0:

            if code:
                client = Client(request.registry, request.cr, SUPERUSER_ID, app, False)
                _json = client.get_openid_by_code(code)

                _logger.info(_json)
                if "errcode" in _json:
                    _logger.warn(u"获取授权信息失败，%s[%s]" % (_json["errmsg"], _json["errcode"]))
                else:
                    user_obj = request.env['tl.weixin.users']
                    user = user_obj.sudo().create_or_update_user_by_openid(app.id, openid)
                    request.session.wx_uid = user.id

            # 没有授权
            if not request.session.wx_uid:
                redirect_url='/%s/%s/account' % (db,app_id)
                localhost_server_url = openerp.tools.config['localhost_server_url']
                db_name = openerp.tools.config['db_name']
                weixin_url = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=%s&redirect_uri=%s/%s/lottery&response_type=code&scope=snsapi_userinfo&state=%s#wechat_redirect' % (
                    app.appid, localhost_server_url, db_name, redirect_url)
                return werkzeug.utils.redirect(weixin_url)


            user_obj = request.env['tl.weixin.users']
            wx_uer = user_obj.sudo().browse(int(request.session.wx_uid))

            #统计用户的奖品数
            result_obj = request.env['born.activity.result']
            domain = [('weixin_user_id', '=', request.session.wx_uid),('activity_gift_id', '!=', False)]
            qty = result_obj.sudo().search_count(domain)

            user_info['phone'] =wx_uer.phone or u'电话未绑定'
            user_info['gift_qty'] = qty
            user_info['name']=wx_uer.name
            user_info['image_url'] = wx_uer.headimgurl
            user_info['gift_url'] = '/%s/gifts' % (db)


        #非微信打开
        return get_template('account.html',account=user_info)


    # 奖品列表
    @http.route(['/<string:db>/gifts'], type='http', auth="none", csrf=False)
    def user_gifts(self, db=None,app_id=None, **post):

        if not request.session.wx_uid:
            errmsg = u'未授权访问'
            return get_template('error.html', errmsg=errmsg)

        user_obj = request.env['tl.weixin.users']
        wx_uer = user_obj.sudo().browse(int(request.session.wx_uid))

        result_obj = request.env['born.activity.result']
        domain = [('weixin_user_id', '=', request.session.wx_uid),('activity_gift_id', '!=', False)]
        gifts = result_obj.sudo().search(domain)

        #非微信打开
        return get_template('gifts.html',gifts=gifts)