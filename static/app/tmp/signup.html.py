# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1464936377.233014
_enable_loop = True
_template_filename = '/opt/odoo-dianshang/born/born_lottery/static/app/signup.html'
_template_uri = 'signup.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\r\n<!DOCTYPE html>\r\n<html lang="en">\r\n<head>\r\n    <meta charset="utf-8"/>\r\n    <title>\u767b\u8bb0\u6ce8\u518c</title>\r\n    <meta name="description" content="\u5e97\u5c1a\u8f6f\u4ef6"/>\r\n    <meta name="keywords"\r\n          content="\u5e97\u5c1a\u8f6f\u4ef6,\u6d3b\u52a8,\u4f2f\u6069\u7f51\u7edc\u79d1\u6280,\u5fae\u5361APP"/>\r\n    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1"/>\r\n    <link rel="stylesheet" href="/born_lottery/static/app/css/bootstrap.css" type="text/css"/>\r\n    <link rel="stylesheet" href="/born_lottery/static/app/css/app.css" type="text/css"/>\r\n    <link rel="stylesheet" href="/born_lottery/static/app/css/weui.min.css" type="text/css"/>\r\n</head>\r\n<body>\r\n<ion-view>\r\n     <div class="weui_cells weui_cells_form">\r\n            <div class="weui_cell ">\r\n                <div class="weui_cell_hd"><label class="weui_label">\u624b\u673a</label></div>\r\n                <div class="weui_cell_bd weui_cell_primary">\r\n                    <input id="phone" name="phone" class="weui_input" type="tel" placeholder="\u8bf7\u8f93\u5165\u624b\u673a\u53f7\u7801">\r\n                </div>\r\n                <div class="weui_cell_ft weui_cell_primary">\r\n                    <button id="getcode" type="button"  class="weui_btn weui_btn_mini weui_btn_primary">\u83b7\u53d6\u9a8c\u8bc1\u7801</button>\r\n                </div>\r\n            </div>\r\n            <div class="weui_cell ">\r\n                <div class="weui_cell_hd"><label class="weui_label">\u9a8c\u8bc1\u7801</label></div>\r\n                <div class="weui_cell_bd weui_cell_primary">\r\n                    <input id="code" name="code"  class="weui_input" type="tel" placeholder="\u8bf7\u8f93\u5165\u77ed\u4fe1\u9a8c\u8bc1\u7801">\r\n                </div>\r\n            </div>\r\n        </div>\r\n</ion-view>\r\n</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"26": 20, "20": 2, "15": 0}, "uri": "signup.html", "filename": "/opt/odoo-dianshang/born/born_lottery/static/app/signup.html"}
__M_END_METADATA
"""
