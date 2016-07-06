#!/bin/env pypy
# -*- coding:utf-8 -*-
# Date:        2016-06-29
# Author:      simonzhang
# web:         www.simonzhang.net
# Email:       simon-zzm@163.com
### END INIT INFO
from json import dumps, loads

# check error
def checkData(data, dataName):
    toJson = {}
    if len(data) <= 0:
        toJson = {"code":"941"}
    else:
        dataNameList = data[0].keys()
        # 
        if dataName not in dataNameList:
            toJson = {"code":"940"}
    return toJson

# Mysql select the data transfer json
# 
def dataToJson(sqlData, dataName):
    #
    checkStatus = checkData(sqlData, dataName)
    if len(checkStatus) > 0:
        return dumps(checkStatus, ensure_ascii = False)
    #
    dataNameList = sqlData[0].keys()
    dataNameList.remove(dataName)
    toJson = {}
    for lo1 in xrange(len(sqlData)):
        tmp = {}
        for lo2 in dataNameList:
            tmp[lo2] = sqlData[lo1][lo2]
        toJson[sqlData[lo1][dataName]] = tmp
    return dumps(toJson, ensure_ascii = False)

# 
def connDataToJson(initData, connField1, 
                   insertData, connField2, dataName='default'):
    '''
    
    '''
    #
    tmpInitData = loads(initData)
    if len(tmpInitData) == 1 and 'code' in tmpInitData.keys():
        reJson = {"code":"940"}
        return dumps(reJson, ensure_ascii = False)
    # 
    tmpInsertData = loads(dataToJson(insertData, connField2))
    tmpInsertDataKeys = tmpInsertData.keys()
    #
    for lineData in tmpInitData:
        tmpConnField =  tmpInitData[lineData][connField1]
        if "%s" % tmpConnField in tmpInsertDataKeys:
            tmpInitData[lineData][dataName] = tmpInsertData["%s" % tmpConnField]
        else:
            tmpInitData[lineData][dataName] = {}
    return dumps(tmpInitData, ensure_ascii = False)
    
 
