# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1464773179.066523
_enable_loop = True
_template_filename = '/opt/odoo-dianshang/born/born_lottery/static/app/error.html'
_template_uri = 'error.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\n<html>\n    <head>\n        <title>\u51fa\u9519\u5566</title>\n        <meta charset="utf-8">\n        <meta http-equiv="X-UA-Compatible" content="IE=edge">\n        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">\n        <meta name="description" content="\u5e97\u5c1a,\u5fae\u5361,\u4f1a\u5458\u7ba1\u7406,\u6ce2\u6069\u81f4\u529b\u4e8e\u63d0\u4f9b\u6700\u51fa\u8272\u7684\u4ea7\u54c1\u548c\u670d\u52a1,\u8ba9\u60a8\u80fd\u6700\u5927\u9650\u5ea6\u5730\u611f\u53d7\u5230\u6211\u4eec\u7684\u70ed\u60c5">\n        <link href="/born_lottery/static/app/css/weui.min.css" rel="stylesheet"/>\n    </head>\n    <body ontouchstart>\n\n        <div class="weui_msg">\n          <div class="weui_icon_area"><i class="weui_icon_warn weui_icon_msg"></i></div>\n          <div class="weui_text_area">\n            <h2 class="weui_msg_title">\u64cd\u4f5c\u5931\u8d25</h2>\n            <p class="weui_msg_desc">\u5185\u5bb9\u8be6\u60c5\uff0c\u975e\u6cd5\u8bf7\u6c42</p>\n          </div>\n          <div class="weui_opr_area">\n\n          </div>\n\n        </div>\n    </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"26": 20, "20": 1, "15": 0}, "uri": "error.html", "filename": "/opt/odoo-dianshang/born/born_lottery/static/app/error.html"}
__M_END_METADATA
"""
