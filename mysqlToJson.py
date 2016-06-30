#!/bin/env pypy
# -*- coding:utf-8 -*-
# Date:        2016-0629
# Author:      simonzhang
# web:         www.simonzhang.net
# Email:       simon-zzm@163.com
### END INIT INFO
from json import dumps

# Mysql select the data transfer json
# 
def dataToJson(sqlData, dataName):
    if len(sqlData) <= 0:
        return dumps('{}')
    dataNameList = sqlData[0].keys()
    # 
    if dataName not in dataNameList:
        return "950"
    # 
    dataNameList.remove(dataName)
    toJson = {}
    for lo1 in xrange(len(sqlData)):
        tmp = {}
        for lo2 in dataNameList:
            tmp[lo2] = sqlData[lo1][lo2]
        toJson[sqlData[lo1][dataName]] = tmp
    return dumps(toJson, ensure_ascii=False)
