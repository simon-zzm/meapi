#!/bin/env pypy
# -*- coding:utf-8 -*-
# Date:        2015-10-14
# Author:      simonzhang
# web:         www.simonzhang.net
# Email:       simon-zzm@163.com
# 引入模块
from modules import *


class exampleHandler(tornado.web.RequestHandler):
    # 认证部分。如果不需要认证，则注释掉下面一行
    #@auth
    def get(self):
        # 获取传入参数。一定要用try包一起来。
        # 避免参数漏传或传错引起系统报错。
        # 测试部分，没有参数就返回所有数据
        try:
            id = self.get_argument("id")
            data = sqlcomm("select username,id from user where id =%s" % id)
        except:
            data = sqlcomm("select username,id from user")
        # 导入查出的数据转json
        # 转部分参数两个，第一个为数据库取出的数据，第二个为做
        # json名字部分的字段名。
        import mysqlToJson
        getJson =  mysqlToJson.dataToJson(data, "username")
        # 获取用户信息数据
        userInfoData = sqlcomm('select userId, age, class from userInfo')
        # 组合json
        # json五个参数，第一个为原始json，第二个为原始json里要链接字段
        # 第三个为要插入的数据，第四个为插入数据要链接的字段
        # 第五个为插入数据在新json里的名字
        getJson = mysqlToJson.connDataToJson(getJson, 'id', \
                                             userInfoData, 'userId', 'info')
        # 转换完成返回
        self.write(getJson)
