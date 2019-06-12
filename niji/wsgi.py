#!/usr/bin/env python
#coding=utf-8
'''
wsgi.py
niji

Created by HTC at 2019-06-12
Copyright © 2019 Efun Company Ltd. All rights reserved.
'''

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

application = get_wsgi_application()
