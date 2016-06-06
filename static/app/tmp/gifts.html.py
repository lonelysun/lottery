# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1465129020.236965
_enable_loop = True
_template_filename = '/opt/odoo-dianshang/born/born_lottery/static/app/gifts.html'
_template_uri = 'gifts.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        gifts = context.get('gifts', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\r\n<!DOCTYPE html>\r\n<html lang="en">\r\n<head>\r\n    <meta charset="utf-8"/>\r\n    <title>\u6211\u7684\u5956\u54c1</title>\r\n    <meta name="description" content="\u5e97\u5c1a\u8f6f\u4ef6"/>\r\n    <meta name="keywords"\r\n          content="\u5e97\u5c1a\u8f6f\u4ef6,\u6d3b\u52a8,\u4f2f\u6069\u7f51\u7edc\u79d1\u6280,\u5fae\u5361APP"/>\r\n    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1"/>\r\n    <link rel="stylesheet" href="/born_lottery/static/app/css/bootstrap.css" type="text/css"/>\r\n    <link rel="stylesheet" href="/born_lottery/static/app/css/font-awesome.min.css" type="text/css"/>\r\n    <link rel="stylesheet" href="/born_lottery/static/app/css/app.css" type="text/css"/>\r\n    <link rel="stylesheet" href="/born_lottery/static/app/css/weui.min.css" type="text/css"/>\r\n</head>\r\n<body>\r\n<ion-view>\r\n    <div id="content">\r\n\r\n        <div class="panel b-a">\r\n        <div class="panel-heading b-b b-light">\r\n          <a href="" class="font-bold">\u5956\u54c1\u5217\u8868</a>\r\n        </div>\r\n        <ul class="list-group list-group-lg no-bg auto">\r\n\r\n')
        for gift in gifts:
            __M_writer(u'                    <li class="list-group-item clearfix">\r\n            <span class="clear">\r\n              <span>')
            __M_writer(unicode(gift.activity_gift_id.gift_id.name))
            __M_writer(u'</span>\r\n              <small class="text-muted clear text-ellipsis">')
            __M_writer(unicode(gift.create_date))
            __M_writer(u'</small>\r\n            </span>\r\n          </li>\r\n\r\n')
        __M_writer(u'\r\n\r\n        </ul>\r\n\r\n      </div>\r\n\r\n    </div>\r\n</ion-view>\r\n</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"34": 28, "15": 0, "21": 2, "22": 27, "23": 28, "24": 30, "25": 30, "26": 31, "27": 31, "28": 36}, "uri": "gifts.html", "filename": "/opt/odoo-dianshang/born/born_lottery/static/app/gifts.html"}
__M_END_METADATA
"""
