# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1465181118.42
_enable_loop = True
_template_filename = 'D:\\pywork\\odoo-9.0\\liuhao\\born_lottery\\static\\app/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        activity = context.get('activity', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\r\n<!DOCTYPE html>\r\n<html lang="en">\r\n<head>\r\n    <meta charset="utf-8"/>\r\n    <title>')
        __M_writer(unicode(activity.active_tpl_id.name))
        __M_writer(u'</title>\r\n    <meta name="description" content="\u5e97\u5c1a\u8f6f\u4ef6"/>\r\n    <meta name="keywords"\r\n          content="\u5e97\u5c1a\u8f6f\u4ef6,\u6d3b\u52a8,\u4f2f\u6069\u7f51\u7edc\u79d1\u6280,\u5fae\u5361APP"/>\r\n    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1"/>\r\n    <link rel="stylesheet" href="/born_lottery/static/app/css/bootstrap.css" type="text/css"/>\r\n    <link rel="stylesheet" href="/born_lottery/static/app/css/app.css" type="text/css"/>\r\n</head>\r\n<body>\r\n<ion-view>\r\n    <div id="content">\r\n\r\n        <div >\r\n            <a href="')
        __M_writer(unicode(activity.game_url))
        __M_writer(u'">\r\n          <img src="')
        __M_writer(unicode(activity.game_id.image_url))
        __M_writer(u'" class="img-full" alt="...">\r\n            </a>\r\n        </div>\r\n        <div id="features" class="bg-white-only">\r\n            <div class="container">\r\n                <div class="list-unstyled  m-t-xl">\r\n                    ')
        __M_writer(unicode(activity.active_tpl_id.description))
        __M_writer(u'\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </div>\r\n</ion-view>\r\n</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"35": 29, "15": 0, "21": 2, "22": 7, "23": 7, "24": 20, "25": 20, "26": 21, "27": 21, "28": 27, "29": 27}, "uri": "index.html", "filename": "D:\\pywork\\odoo-9.0\\liuhao\\born_lottery\\static\\app/index.html"}
__M_END_METADATA
"""
