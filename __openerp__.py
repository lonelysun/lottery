# -*- coding: utf-8 -*-
##############################################################################
#  COMPANY: BORN
#  AUTHOR: KIWI
#  EMAIL: arborous@gmail.com
#  VERSION : 1.0   NEW  2014/07/21
#  UPDATE : NONE
#  Copyright (C) 2011-2014 www.wevip.com All Rights Reserved
##############################################################################
{
    'name': '店尚活动',
    'version': '1.0.1',
    'category': 'BORN',
    'sequence': 1,
    'summary': 'BORN',
    'description': """
          店尚活动
    """,
    'author': 'BORN',
    'images': [],
    'depends': ['base','account','tl_weixin'],
    'data': [
        'born_lottery.xml',
        #'security/ir.model.access.csv',
    ],
    'css': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}