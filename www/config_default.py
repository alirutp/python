#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default configurations.
'''

__author__ = 'Michael Liao'

configs = {
    'debug': True,
    'db': {
        'host': '192.168.11.226',
        'port': 3306,
        'user': 'wpad',
        'password': '111111',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}
