# !/usr/bin/python
# -*- encoding: utf-8 -*-
# @author:spider1998
import random
from settings import USER_AGENTS
from settings import PROXIES
import base64

class RandomUserAgent(object):
    def process_request(self,request,spider):
        useragent = random.choice(USER_AGENTS)
        request.headers.setdefault("User-Agent",useragent)

class RandomProxy(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)
        if proxy['user_passwd'] is None:
            #没有代理账户验证的代理使用方式
            request.meta['proxy'] = "http:// + proxy['ip_port']"
        else:
            base64_userpasswd = base64.b64encode(proxy['user_passwd'])
            request.meta['proxt'] = "http:// + proxy['ip_port']"
            request.headers['Proxy-Authorization'] = 'Basic ' + base64_userpasswd

