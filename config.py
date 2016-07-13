#!/bin/env python
# -*- coding: utf-8 -*-
# Filename:    config.py
# Date:        2015-10-01
# Author:      simonzhang
# web:         www.simonzhang.net
# Email:       simon-zzm@163.com
### END INIT INFO

# 监听部分
listenIp = '182.92.186.219'
listenPort = 55000

# SSL部分，实现https
# 将私钥和签名文件放到项目跟目录下即可
# 如果不需要此项为空
crtFile = '' 
keyFile = ''

# cookie 安全 key
cookieKey = 'dfK8Wv6fgDew+6UGVRBhcbVekWBQc80FKsTF$CsYCiitG'
sessionTimeout = 60*60*24*7

# mysql
# 单个数据库信息格式为：IP 端口 账号 密码 库名
# 多个库以列表形势配置
MySqlWriteInfo = [['10.171.53.171', 3306, 'caidanium', '4f8f$e8f', 'caidaniu'],]
MySqlReadInfo = [['10.171.53.171', 3306, 'caidanium', '4f8f$e8f', 'caidaniu'],]

# redis 数据超时时间为7天
redisIp = "10.171.53.171"
redisPort = "6379"
reidsTimeout = 60*60*24*7

# 慢日志
# 当前接口超时n秒后记录慢日志
# 慢日志默认位置在logs目录下，文件名为slow.log(未测试)
slowTimeout = 2

# 日志路径
logPath = './logs/'

# 黑白名单那设置
blackList = []
whiteList = []

# 美秒中可以访问的次数
secondRate = 0
