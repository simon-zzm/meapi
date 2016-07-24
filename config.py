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

# 调试模式为True。代码错误会打印到浏览器上，代码修改后立即生效
# 运行模式为False。执行速度快，但是代码修改后需要重启服务。
debugMode = False

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

# 如果要记录日志，需要使用toWrite返回数据
# 慢日志
# 当前接口超时n秒后记录慢日志
# 慢日志默认位置在logs目录下，文件名为slow.log(未测试)
slowTimeout = 2

# 记录详细日志(默认关闭)
# true为开启，False为关闭
# 日志格式:请求时间 远程ip 返回耗时 请求地址 请求协议 请求模式 请求路径 浏览器信息
logStatus = True

# 日志路径
logPath = './logs/'

# 黑白名单那设置
# 格式为['192.168.1.1', '192.168.1.2']
# 如果为'0.0.0.0'为所有
blackList = []
whiteList = []

# 每秒中可以访问的次数（未实现）
secondRate = 0

# 防SQL注入关键字。只在modules.py中使用。
sqlInjData = ["'", 'and', 'or', 'exec', 'insert', 
              'select', 'delete', 'update', 'count', 
              'chr', 'mid', 'master', 'truncate', 'char', 
              'declare', '=', '{', '}', '[', ']', '\\', 
              ':', ';', '<', '>', '?', ',', '.', '`', '~', 
              '!', '@', '$', '*', '%', '^', '(', ')', 
              '|', 'script']
