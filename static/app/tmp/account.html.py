# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1465197882.641
_enable_loop = True
_template_filename = 'D:\\pywork\\odoo-9.0\\liuhao\\born_lottery\\static\\app/account.html'
_template_uri = 'account.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        account = context.get('account', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\r\n<!DOCTYPE html>\r\n<html lang="en">\r\n<head>\r\n    <meta charset="utf-8"/>\r\n    <title>\u4e2a\u4eba\u4e2d\u5fc3</title>\r\n    <meta name="description" content="\u5e97\u5c1a\u8f6f\u4ef6"/>\r\n    <meta name="keywords"\r\n          content="\u5e97\u5c1a\u8f6f\u4ef6,\u6d3b\u52a8,\u4f2f\u6069\u7f51\u7edc\u79d1\u6280,\u5fae\u5361APP"/>\r\n    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1"/>\r\n    <link rel="stylesheet" href="/born_lottery/static/app/css/bootstrap.css" type="text/css"/>\r\n    <link rel="stylesheet" href="/born_lottery/static/app/css/font-awesome.min.css" type="text/css"/>\r\n\r\n    <link rel="stylesheet" href="/born_lottery/static/app/css/app.css" type="text/css"/>\r\n    <link rel="stylesheet" href="/born_lottery/static/app/css/weui.css" type="text/css"/>\r\n</head>\r\n<body style="background-color: #f6f7f7">\r\n<ion-view>\r\n    <div style="padding-top:40px;">\r\n        <a href="" class="avatar b-3x" style="width: 75px;margin-left:auto;margin-right: auto;">\r\n            <img src="')
        __M_writer(unicode(account['image_url']))
        __M_writer(u'" alt="...">\r\n        </a>\r\n        <div class="text-center" style="font-size: 20px;margin-top:15px">\r\n            ')
        __M_writer(unicode(account['name']))
        __M_writer(u'\r\n        </div>\r\n        <div class="text-center" style="font-size: 14px;color:#9b9b9b">\r\n            \u5fae\u4fe1\u7528\u6237\uff0c\u4eab\u53d7\u66f4\u4f18\u8d28\u7684\u670d\u52a1')
        __M_writer(unicode(account['phone']))
        __M_writer(u'\r\n        </div>\r\n    </div>\r\n\r\n    <div class="weui_cells weui_cells_access">\r\n\r\n        <a class="weui_cell" href="javascript:;">\r\n          <div class="weui_cell_hd"><img src="/born_lottery/static/app/quan.png" alt="" style="width:22px;margin-right:15px;display:block"></div>\r\n          <div class="weui_cell_bd weui_cell_primary" style="font-size: 16px">\r\n            <p style="margin: 0;">\u6211\u7684\u4f18\u60e0\u5238</p>\r\n          </div>\r\n          <div class="weui_cell_ft"></div>\r\n        </a>\r\n\r\n        <a class="weui_cell" href="javascript:;">\r\n          <div class="weui_cell_hd"><img src="/born_lottery/static/app/tuan.png" alt="" style="width:22px;margin-right:15px;display:block"></div>\r\n          <div class="weui_cell_bd weui_cell_primary" style="font-size: 16px">\r\n            <p style="margin: 0;">\u6211\u7684\u62fc\u56e2</p>\r\n          </div>\r\n          <div class="weui_cell_ft"></div>\r\n        </a>\r\n\r\n        <a class="weui_cell" href="javascript:;">\r\n          <div class="weui_cell_hd"><img src="/born_lottery/static/app/quan.png" alt="" style="width:22px;margin-right:15px;display:block"></div>\r\n          <div class="weui_cell_bd weui_cell_primary" style="font-size: 16px">\r\n            <p style="margin: 0;">\u6211\u7684\u56e2\u8d2d\u5238</p>\r\n          </div>\r\n          <div class="weui_cell_ft"></div>\r\n        </a>\r\n\r\n        <a class="weui_cell" href="javascript:;">\r\n          <div class="weui_cell_hd"><img src="/born_lottery/static/app/hongbao.png" alt="" style="width:22px;margin-right:15px;display:block"></div>\r\n          <div class="weui_cell_bd weui_cell_primary" style="font-size: 16px">\r\n            <p style="margin: 0;">\u6211\u7684\u7ea2\u5305</p>\r\n          </div>\r\n          <div class="weui_cell_ft"></div>\r\n        </a>\r\n\r\n        <a class="weui_cell" href="')
        __M_writer(unicode(account['gift_url']))
        __M_writer(u'">\r\n          <div class="weui_cell_hd"><img src="/born_lottery/static/app/gift.png" alt="" style="width:22px;margin-right:15px;display:block"></div>\r\n          <div class="weui_cell_bd weui_cell_primary" style="font-size: 16px">\r\n            <p style="margin: 0;">\u6211\u7684\u5956\u54c1<span style="color:#9b9b9b">&nbsp;&nbsp;&nbsp;(')
        __M_writer(unicode(account['gift_qty']))
        __M_writer(u')</span></p>\r\n          </div>\r\n          <div class="weui_cell_ft"></div>\r\n        </a>\r\n\r\n      </div>\r\n\r\n\r\n</ion-view>\r\n</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"37": 31, "15": 0, "21": 2, "22": 22, "23": 22, "24": 25, "25": 25, "26": 28, "27": 28, "28": 66, "29": 66, "30": 69, "31": 69}, "uri": "account.html", "filename": "D:\\pywork\\odoo-9.0\\liuhao\\born_lottery\\static\\app/account.html"}
__M_END_METADATA
"""
