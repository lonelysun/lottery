# -*- coding: utf-8 -*-
##############################################################################
#  COMPANY: BORN
#  AUTHOR: LIUHAO
#  EMAIL: arborous@gmail.com
#  VERSION : 2.0    2016/05/20
#  UPDATE : NONE
#  Copyright (C) 2011-2014 www.wevip.com All Rights Reserved
##############################################################################

import openerp
from openerp.osv import fields, osv
from openerp import models, fields, api
from openerp import _
import logging
import uuid
import json
import random
import time
import io
import base64
from tools.s3client import s3client
import hashlib
import openerp
import string
from openerp import SUPERUSER_ID
import random
from openerp.addons.tl_weixin.tools.client import Client

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

try:
    import qrcode
except ImportError:
    qrcode = None

import openerp.addons.decimal_precision as dp

_logger = logging.getLogger(__name__)


# 活动
class born_activity_tpl(osv.osv):
    _name = 'born.activity.tpl'
    _description = u"模板"

    name = fields.Char(u'名称', size=255, help=u"活动名称", required=True)
    image = fields.Binary(string=u"活动海报", attachment=True, help=u"活动海报")
    image_url=fields.Char(u'海报地址', size=255, help=u"海报地址")
    file_name=fields.Char(u'海报名称', size=255, help=u"海报名称")
    note = fields.Text(u'活动简介', required=True, help=u'活动简介')
    description = fields.Text(u'活动描叙', required=True, help=u'活动详细描叙,活动参与流程')
    provision = fields.Text(u'活动条款', help=u'参与活动的条款')
    active = fields.Boolean(u'归档', default=True)
    price = fields.Float(u'报名费', help=u'参与活动的报名费用')
    company_id = fields.Many2one('res.company', u'公司', ondelete='cascade', required=True, help=u'活动所属公司')
    game_id = fields.Many2one('born.game', u'游戏', help=u'参与活动的游戏')
    app_id = fields.Many2one('tl.weixin.app', u'公众号', ondelete="cascade")
    activity_ids = fields.One2many('born.activity', 'active_tpl_id', string=u'活动', help=u'商户报名活动列表')
    company_ids = fields.Many2many('res.company', 'born_activity_company_rel', 'activity_id', 'company_id', u'允许发行的公司',
                               help=u'限制该活动允许发行的公司,不设置表示所有的平台都可以看到该活动')
    default_gift_ids = fields.Many2many('born.game.gift', 'born_activity_default_gift_rel', 'activity_id', 'gift_id',
                                    u'默认奖品', help=u'该奖品为发行活动的公司提供,所有参与的公司都能够使用该奖品')

    @api.model
    def create(self, vals):

        if vals.get('image',False):
            s3 = s3client(self)
            image_url = s3.upload(self._cr, self._uid,  vals.get('image'), vals.get('file_name', 'image.png'))
            vals['image_url'] = image_url
        return super(born_activity_tpl, self).create(vals)

    @api.multi
    def write(self, vals):

        if vals.get('image', False):
            s3 = s3client(self)
            image_url = s3.upload(self._cr, self._uid, vals.get('image'), vals.get('file_name', 'image.png'))
            vals['image_url'] = image_url
        return super(born_activity_tpl, self).write(vals)


# 游戏
class born_game(osv.osv):
    _name = 'born.game'
    _description = u"游戏"

    name = fields.Char(u'名称', size=255, help=u"游戏名称", required=True, )
    note = fields.Text(u'简介', size=255, required=True, help=u"简介")
    path = fields.Char(u'文件夹名称', size=255, required=True, help=u"文件夹名称")
    image_url = fields.Char(u'海报地址', size=255, help=u"海报地址")
    file_name = fields.Char(u'海报名称', size=255, help=u"海报名称")
    image = fields.Binary(string=u"游戏海报", required=True, attachment=True, help=u"游戏海报")
    description = fields.Text(u'玩法说明', required=True, help=u"游戏玩法和说明")

    @api.model
    def create(self, vals):

        if vals.get('image', False):
            s3 = s3client(self)
            image_url = s3.upload(self._cr, self._uid,  vals.get('image'), vals.get('file_name', 'image.png'))
            vals['image_url'] = image_url
        return super(born_game, self).create(vals)

    @api.multi
    def write(self, vals):

        if vals.get('image', False):
            s3 = s3client(self)
            image_url = s3.upload(self._cr, self._uid, vals.get('image'), vals.get('file_name', 'image.png'))
            vals['image_url'] = image_url
        return super(born_game, self).write(vals)



# 游戏
class born_game_gift(osv.osv):
    _name = 'born.game.gift'
    _description = u"游戏奖品"

    name = fields.Char(u'名称', size=255, required=True, help=u"游戏名称")
    image = fields.Binary(string=u"图片", attachment=True, help=u"图片")
    product_id = fields.Many2one('product.product', string=u'产品', ondelete='cascade', help=u'商品')
    wxcard_id = fields.Many2one('tl.wxcard', string=u'微信优惠券', ondelete='cascade', help=u'微信优惠券')
    redpack_amount = fields.Float(string=u"微信红包金额", digits=(2, 0), help=u'发送微信现金红包')

    description = fields.Text(u'说明', help=u"奖品说明")


# 付款
class born_activity_payment(osv.osv):
    _name = 'born.activity.payment'
    _description = u"付款"
    _rec_name = "serial_number"

    activity_id = fields.Many2one('born.activity', string=u'报名', ondelete='cascade', help=u'活动报名')
    amount = fields.Float(string=u'支付金额', help=u'支付金额')
    journal_id = fields.Many2one('account.journal', string=u'支付方式', ondelete='cascade',
                                 help=u"支付方式")
    serial_number = fields.Char(u'交易流水号', size=255, help=u"流水号")


# 活动报名
class born_activity(osv.osv):
    _name = 'born.activity'
    _description = u"活动报名"
    _rec_name = "active_tpl_id"

    @api.one
    @api.depends('active_tpl_id')
    def _compute_url(self):
        for line in self:
            localhost_server_url = openerp.tools.config['localhost_server_url']
            db_name = openerp.tools.config['db_name']
            if line.active_tpl_id.app_id:
                weixin_url = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=%s&redirect_uri=%s/%s/lottery&response_type=code&scope=snsapi_userinfo&state=%s#wechat_redirect' % (
                    line.active_tpl_id.app_id.appid, localhost_server_url, db_name, line.born_uuid)
                line.weixin_url = weixin_url
                _logger.info(line.weixin_url)
            game_url = '%s/%s/activity_game/%s' % (localhost_server_url, db_name, line.born_uuid)
            line.game_url = game_url
            activity_url='%s/%s/lottery?key=%s' % (localhost_server_url, db_name, line.born_uuid)
            line.activity_url = activity_url

    active_tpl_id = fields.Many2one('born.activity.tpl', u'模板', required=True, ondelete='cascade', help=u'模板')
    company_id = fields.Many2one('res.company', u'公司', ondelete='cascade', required=True, help=u'报名参加活动的公司')
    user_id = fields.Many2one('res.users', u'报名者', ondelete='cascade', required=True, help=u'报名参加活动的用户')
    gift_ids = fields.One2many('born.activity.gift', 'activity_id', string=u'奖品', help=u'活动奖品列表')
    explanation = fields.Text(u'规则', help=u'活动规则,奖品领取说明')
    born_uuid = fields.Char(u'唯一码', size=128, help=u"唯一码")
    hits = fields.Float(u'点击量', size=128, help=u"活动链接点击量")
    status = fields.Selection(
        [('draff', u'草稿'), ('preparing', u'未开始'), ('processing', u'进行中'), ('cancel', u'取消 '), ('finish', u'已完成 ')],
        string=u'状态', default="preparing",
        help=u"活动状态", required=True)
    activity_url = fields.Char(string=u'活动链接', compute='_compute_url', multi='_compute_url', help=u"活动入口链接")
    banner = fields.Binary(string=u"海报", attachment=True, help=u"自定义活动海报")
    activity_url_qrcode=fields.Binary(string=u"活动链接二维码", attachment=True, help=u"活动链接二维码")
    app_id = fields.Many2one('tl.weixin.app', u'公众号', ondelete="cascade")
    is_force_regist = fields.Boolean(u'采集手机号码')
    weixin_url = fields.Char(string=u'微信链接', compute='_compute_url',
                             multi='_compute_url', help=u"微信链接")
    game_id = fields.Many2one('born.game', related='active_tpl_id.game_id')
    game_url = fields.Char(string=u'游戏链接', compute='_compute_url', multi='_compute_url', help=u"游戏链接")
    game_chance = fields.Integer(u'抽奖机会', help=u'每个人允许的抽奖次数', default=1)
    payment_id = fields.Many2one('born.activity.payment', string=u'支付信息', help=u'报名活动的支付信息')
    join_ids = fields.One2many('born.activity.result', 'activity_id', string=u'参与情况', help=u'活动的参与情况')
    join_price_ids = fields.One2many('born.activity.result', 'activity_id',domain=[('activity_gift_id','!=',False)] ,string=u'参与情况', help=u'活动的参与情况')
    product_id = fields.Many2one('product.product', u'商品', ondelete='cascade',  help=u'销售的商品')
    product_image = fields.Binary(string=u"商品海报", attachment=True, help=u"商品海报")

    @api.model
    def create(self, vals):

        born_uuid = '%s%s' % (int(time.time()), random.randint(100, 999))
        vals['born_uuid'] = born_uuid
        localhost_server_url = openerp.tools.config['localhost_server_url']
        db_name = openerp.tools.config['db_name']
        code_value='%s/%s/lottery?key=%s' % (localhost_server_url, db_name, born_uuid)
        qr_code = qrcode.QRCode(version=4, box_size=4, border=1)
        qr_code.add_data(code_value)
        qr_code.make(fit=True)
        qr_img = qr_code.make_image()
        output = io.BytesIO()
        qr_img.save(output, 'PNG')
        output.seek(0)
        output_s = output.read()
        b64 = base64.b64encode(output_s)
        vals['activity_url_qrcode']=b64
        return super(born_activity, self).create(vals)


# 活动奖品情况
class born_activity_gift(osv.osv):
    _name = 'born.activity.gift'
    _description = u"活动奖品情况"


    @api.one
    @api.depends('line_ids')
    def _compute_num(self):
        for line in self:
            use_num = 0
            for item in line.line_ids:
                use_num += 1
            line.remain_qty = line.qty - use_num

    name = fields.Char(u'名称', size=255,required=True, help=u"名称")
    activity_id = fields.Many2one('born.activity', required=True, string=u'活动', ondelete='cascade', help=u'活动')
    gift_id = fields.Many2one('born.game.gift', required=True, string=u'奖品', ondelete='cascade', help=u'奖品')
    level = fields.Selection(
        [(1, u'一等奖'), (2, u'二等奖'), (3, u'三等奖'), (4, u'四等奖 '), (5, u'五等奖 '), (6, u'六等奖 ')],
        string=u'几等奖', default=3,
        help=u"标记为几等奖", required=True)
    qty = fields.Integer(u'数量', help=u"奖项的数量")
    probability = fields.Float(u'概率', help=u"概率")
    note = fields.Char(u'说明', size=255, help=u"说明")
    line_ids = fields.One2many('born.activity.result', 'activity_gift_id', string=u'中奖情况', help=u'中奖情况')
    remain_qty = fields.Integer(string=u'剩余数量', compute='_compute_num',
                                multi='_compute_num', help=u"该奖项的剩余中奖次数")

    _sql_constraints = [
        ('unique_activity_gift', 'unique (activity_id,level)', u'奖项不能重复!'),
    ]


# 参与情况
class born_activity_result(osv.osv):
    _name = 'born.activity.result'
    _description = u"参与情况"
    _order = 'id desc'

    @api.one
    @api.depends('partner_id','weixin_user_id')
    def _compute_customer_name(self):
        for line in self:
            if line.weixin_user_id:
                line.name=line.weixin_user_id.name
            elif line.partner_id:
                line.name = line.partner_id.name

    activity_id = fields.Many2one('born.activity', string=u'活动',required=True, ondelete='cascade', help=u'活动')
    partner_id = fields.Many2one('res.partner', string=u'客户', ondelete='cascade', help=u'客户')
    weixin_user_id = fields.Many2one('tl.weixin.users', required=True, string=u'微信用户')
    activity_gift_id = fields.Many2one('born.activity.gift', string=u'奖品', ondelete='cascade', help=u'活动奖品')
    payment_id = fields.Many2one('born.activity.payment', string=u'支付信息', help=u'支付信息')
    name = fields.Char(string=u'客户', compute='_compute_customer_name',
                                multi='_compute_customer_name', help=u"客户")
    card_ext= fields.Char(string=u'卡券签名数据', help=u"卡券签名数据")
    redpack_id = fields.Many2one('tl.weixin.redpack', string=u'红包编号', help=u'红包编号')

    @api.model
    def create(self, vals):

        gift= super(born_activity_result, self).create(vals)

        #微信优惠券
        if gift.activity_gift_id and gift.activity_gift_id.gift_id.wxcard_id:
            client_obj = Client(self.pool, self._cr, self._uid, gift.activity_gift_id.gift_id.wxcard_id.app_id, False)
            jsapi_ticket = client_obj.api_ticket()
            timestamp = int(time.time())
            nonce_str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))
            wxcard_id = gift.activity_gift_id.gift_id.wxcard_id.wxcard_id
            sign_data = [timestamp, nonce_str, wxcard_id, jsapi_ticket]
            sign_data = sorted(sign_data)
            data_str = ''.join(['%s' % (key) for key in sorted(sign_data)])
            signature = hashlib.sha1(data_str).hexdigest()
            outer_id = self.env['ir.sequence'].sudo().next_by_code('outer.id')
            card_ex_data = {
                'nonce_str': nonce_str,
                'timestamp': timestamp,
                'signature': signature,
                'outer_id': outer_id
            }
            card_ext = json.dumps(card_ex_data)
            _logger.info(card_ext)
            gift.card_ext=card_ext

        elif gift.activity_gift_id.gift_id.redpack_amount>0 and gift.weixin_user_id and gift.activity_id.app_id:
            #红包
            redpack_obj = self.env['tl.weixin.redpack']

            vals={
                'act_name':u'恭喜您中奖啦',
                'app_id':gift.activity_id.app_id.id,
                'users_id':gift.weixin_user_id.id,
                'total_amount':gift.activity_gift_id.gift_id.redpack_amount,
                'wishing':u'祝您生意兴隆,财源广进',
                'remark':u'店尚抽奖活动',
                'send_name':gift.activity_id.app_id.name
            }
            redpack_obj.sudo().create(vals)

        return gift





# 账户
class born_account(osv.osv):
    _name = 'born.account'
    _description = u"账户"
    _rec_name = "user_id"

    user_id = fields.Many2one('res.users', u'报名者', ondelete='cascade', required=True, help=u'报名参加活动的用户')
    amount = fields.Float(string=u'金额', help=u'账户金额')
    point = fields.Float(string=u'积分', help=u'积分')
    line_ids = fields.One2many('born.account.line', 'account_id', string=u'账户履历', help=u'账户资金变动履历')


# 账户履历
class born_account_line(osv.osv):
    _name = 'born.account.line'
    _description = u"账户履历"
    _rec_name = "account_id"

    account_id = fields.Many2one('born.account', string=u'账户', ondelete='cascade', required=True, help=u'报名参加活动的用户')
    amount = fields.Float(string=u'金额', help=u'金额')
    point = fields.Float(string=u'积分', help=u'积分')
    type = fields.Selection([('recharge', u'充值'), ('withdraw', u'提现'), ('consume', u'消费'), ('transfer', u'转账 ')],
                            string=u'方式', help=u"账户金额变动方式", required=True)


# 客户
class born_res_partner(models.Model):
    _inherit = "res.partner"

    activity_id = fields.Many2one('born.activity', string=u'活动', ondelete='cascade', help=u'活动')
    is_lottery = fields.Boolean(u'活动玩家', default=False, help=u"标记该用户为参加活动的玩家")
