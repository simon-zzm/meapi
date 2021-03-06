#!/bin/env pypy
# -*- coding:utf-8 -*-
# Date:        2015-10-01
# Author:      simonzhang
# web:         www.simonzhang.net
# Email:       simon-zzm@163.com
### END INIT INFO
import tornado.ioloop
import tornado.web

import sys
import time
import json
import uuid
from config import *

# 登陆
class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            userName = self.get_argument("user")
        except:
            userName = ""
        try:
            passWord = self.get_argument("passwd")
        except:
            passWord = ""
        try:
            passwd = sqlcomm("select passwd from user where username= '%s'" % userName)[0]['passwd']
        except:
            res = {"code":995}
            self.write(dictToJson(res))
            return
        # 验证账号密码
        if checkPasswd(passwd, passWord):
            sessionId = str(uuid.uuid3(uuid.uuid1(), str(userName)))
            self.set_secure_cookie("sessionid", sessionId, \
                                           path="/", expires_days = sessionTimeout)
            if redisDB.setex("%s" % sessionId,  reidsTimeout, "%s" % userName):
                res = {"code":999}
            else:
                res = {"code":997}
        else:
            try:
                sessionId = self.get_secure_cookie("sessionid")
                redisDB.delete("%s" % sessionId)
            except:
                pass
            self.clear_all_cookies()
            res = {"code":995}
        self.write(dictToJson(res))

# 注销部分
class LogoutHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            _sessionId = self.get_secure_cookie("sessionid")
        except:
            _sessionId = ""
        try:
            delRedisStatus = redisDB.delete("%s" % _sessionId)
        except:
            pass
        response = {"code":998}
        self.write(dictToJson(res))

#### 全局模块部分
# 基础认证
def auth(method):
    def checkUser(self, *args, **kwargs):
        _sessionId = self.get_secure_cookie("sessionid")
        try:
            if len(redisDB.get("%s" % _sessionId)) < 3:
                self.clear_all_cookies()
                self.redirect("/")
            else:
                return method(self, *args, **kwargs)
        except:
            self.clear_all_cookies()
            self.redirect("/")
    return checkUser

#### 检查请求url
def checkUrl(method):
    '''
    当前包含检查有
    sql注入
    黑白名单
    '''
    def toCheck(self, *args, **kwargs):
        tmpRes = checkIP(self)
        if len(tmpRes) > 0:
            self.write(tmpRes)
            return 
        tmpRes = sqlInj(self)
        if len(tmpRes) > 0:
            self.write(tmpRes)
            return 
        else:
            return method(self, *args, **kwargs)
    return toCheck

#### 检查IP
def checkIP(self):
    response = ''
    getIP = self.request.remote_ip
    if getIP in whiteList:
        return response
    elif getIP in blackList or '0.0.0.0' in blackList:
        return dictToJson({"code":922})
    else:
        return response

#### 防sql注入
def sqlInj(self):
    response = ''
    try:
        allArgs = self.request.arguments
        for one in allArgs:
            # 获取参数转小写
            tmpArg = self.get_argument(one).lower()
            # 去空格
            tmpArg = tmpArg.replace(' ', '')
            # 检查是否有注入字符串
            for singleInj in sqlInjData:
                if tmpArg.find(singleInj) > -1:
                    # 处理结果
                    res = {"code":921}
                    return dictToJson(res)
    except:
        res = {"code":920}
    return dictToJson(res)

# 将MySQL的数据转为json
def mysqltojson(getList):
    import simplejson
    _createStr = []
    # 循环所有数据字典
    for l in getList:
        # 循环转换所有数据
        _createTmpDict = {}
        for o in l.keys():
            _createTmpDict[o] = l[o]
        _createStr.append(_createTmpDict)
    return simplejson.dumps(_createStr, ensure_ascii=False)

# 将字典转为json
def dictToJson(tmpStr):
    return json.dumps(tmpStr, ensure_ascii=False, sort_keys=True, separators=(',', ':'))

# 加密、解密
from werkzeug.security import generate_password_hash, check_password_hash
def toPasswd(passstr):
    return  generate_password_hash("%s" % passstr)

def checkPasswd(passwd, passstr):
    return check_password_hash("%s" % passwd,"%s" % passstr)


# 获取当时间
# 格式化为 年月日 小时分秒
def getNowTime():
    return time.strftime('%Y-%m-%d %T',time.localtime(time.time()))


# 处理返回数据
def toWrite(self, context):
    #只判断单位为秒
    useTime = int(self.request.request_time())
    if slowTimeout < useTime:
        slowLog = open("%sslow.log" % logPath, "ab")
        slowLog.write("%s %s %s\n" % (getNowTime(), useTime, self.request.uri))
        slowLog.close()
    if logStatus :
        nowTime = getNowTime()
        getIP = self.request.remote_ip
        getUri = self.request.uri
        getAgent = self.request.headers['User-Agent']
        getHost = self.request.host
        getProtocol =self.request.protocol
        getMethod = self.request.method
        log = open('%slog%s.log' % (logPath, nowTime.split()[0]), "ab")
        log.write('%s %s %s %s %s %s %s "%s"\n' % (nowTime, getIP, useTime,
                                                   getHost, getProtocol, 
                                                   getMethod, getUri, getAgent))
        log.close()
    self.write(context)


#### 数据库部分
import torndb
# write database
wdbInfo = MySqlWriteInfo[0]
wdb = torndb.Connection("%s:%s" % (wdbInfo[0], wdbInfo[1]), \
                                      wdbInfo[4], \
                                      wdbInfo[2], \
                                      wdbInfo[3])

# read database
rdbInfo = MySqlReadInfo[0]
rdb = torndb.Connection("%s:%s" % (rdbInfo[0],rdbInfo[1]), \
                                      rdbInfo[4], \
                                      rdbInfo[2], \
                                      rdbInfo[3])
# 执行sql，并简单判断返回值类型。
# 如果是插入、更新、删除返回值为执行的id
def sqlcomm(sql):
    if sql.split()[0].lower() == "select":
        data = rdb.query(sql)
    else:
        data = wdb.execute_lastrowid(sql)
    return data


#### redis
import redis
redisDB = redis.StrictRedis(host = redisIp, port = redisPort, db=redisDB)
#redis_db.setex("key", redis_timeout, "valuse")
#redis_db.get("key")

#### 系统部分
class BaseErrorHandler(tornado.web.RequestHandler):
    def write_error(self, status_code, **kwargs):
        self.writeError(status_code, **kwargs)
    
    def writeError(self, statusCode, **kwargs):
        if statusCode == 405:
            self.write(dictToJson({"code":960}))
        else:
            self.write(dictToJson({"code":statusCode}))
