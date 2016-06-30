#!/bin/env python
# -*- coding: utf-8 -*-
# Filename:    config.py
# Date:        2015-10-01
# Author:      simonzhang
# web:         www.simonzhang.net
# Email:       simon-zzm@163.com
### END INIT INFO

# 监听部分
listenIp = 'x.x.x.x'
listenPort = 55000

# SSL部分，实现https
# 将私钥和签名文件放到项目跟目录下即可
# 如果不需要此项为空
crtFile = '' 
keyFile = ''

# cookie 安全 key。随便写
cookieKey = 'dfK8Wv6fgDew+6UGm#Bhc$dekWBQc80FKsTF$CsOCi3tG'
sessionTimeout = 60*60*24*7

# mysql
# 单个数据库信息格式为：IP 端口 账号 密码 库名
# 多个库以列表形势配置
MySqlWriteInfo = [['x.x.x.x', 3306, 'meapi', 'xxxxxx', 'meapi'],]
MySqlReadInfo = [['x.x.x.x', 3306, 'meapi', 'xxxxxx', 'meapi'],]

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
