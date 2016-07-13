#!/bin/env pypy
# -*- coding:utf-8 -*-
# Author:      simonzhang
# web:         www.simonzhang.net
# Email:       simon-zzm@163.com
#                   _ooOoo_
#                  o8888888o
#                  88" . "88
#                  (| -_- |)
#                  O\  =  /O
#               ____/`---'\____
#             .'  \\|     |//  `.
#            /  \\|||  :  |||//  \
#           /  _||||| -:- |||||-  \
#           |   | \\\  -  /// |   |
#           | \_|  ''\---/''  |   |
#           \  .-\__  `-`  ___/-. /
#         ___`. .'  /--.--\  `. . __
#      ."" '<  `.___\_<|>_/___.'  >'"".
#     | | :  `- `.;`\ _ /`;.`/ - ` : | |
#     \  \ `-.   \_ __\ /__ _/   .-` /  /
#======`-.____`-.___\_____/___.-`____.-'======
#                   `=---='
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#  佛祖保佑 代码高性能 不宕机 无bug
### END INIT INFO
import tornado.httpserver
import tornado.ioloop
import tornado.web

import os
import ssl
import sys
import uuid
from config import *

from route import *

settings = {
    "cookie_secret": cookieKey,
    "xsrf_cookies":True,
    "login_url": "/",
    "static_path":"static",
    "debug":True,
}

if __name__ == "__main__":
    # 安全https部分
    if len(crtFile) != 0 or len(keyFile) != 0:
        try:
            application = tornado.httpserver.HTTPServer(
                              application,ssl_options={
                                  "certfile": "%s" % crtFile, 
                                  "keyfile": "%s" % keyFile}
                              )
        except:
            print "https 配置文件部分错误"
            exit()
    application.listen(listenPort, "%s" % listenIp)
    tornado.ioloop.IOLoop.instance().start()
