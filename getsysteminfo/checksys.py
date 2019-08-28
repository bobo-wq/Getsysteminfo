
import json
#
import  accessinfo
import  access_sql
import requests
import os
import fnmatch
import subprocess


def cpu(cpuinfo):
    result = []
    for i in range(len(cpuinfo)):

        if int(cpuinfo[i][2]) >= 85:
            content="{} {}的cpu已经使用到极限了,cpuused:{}%".format(cpuinfo[i][0],cpuinfo[i][1],cpuinfo[i][2])
            senddingtalk(content)
            access_log(i,cpuinfo,content)
        else:
            content = "{} {}的cpu正常,cpuused:{}%".format(cpuinfo[i][0], cpuinfo[i][1], cpuinfo[i][2])
        result.append(content)
    return result


def memory(memoryinfo):
    reslut=[]
    for i in range(len(memoryinfo)):
        if int(memoryinfo[i][2]) >= 90:
            content="{} {}的内存已经使用到极限了,memoryused:{}%".format(memoryinfo[i][0],memoryinfo[i][1],memoryinfo[i][2])
            senddingtalk(content)
            access_log(i, memoryinfo, content)
        else:
            content="{} {}的内存正常,memoryused:{}%".format(memoryinfo[i][0],memoryinfo[i][1],memoryinfo[i][2])
        reslut.append(content)
    return reslut

def disk(diskinfo):
    result=[]
    for i in range(len(diskinfo)):
        if int(diskinfo[i][2].replace('%','')) >= 60:
            content="{} {}的磁盘已经使用到极限了,diskused:{}".format(diskinfo[i][0],diskinfo[i][1],diskinfo[i][2])
            senddingtalk(content)
            access_log(i, diskinfo, content)
        else:
            content="{} {}的磁盘正常,diskused{}".format(diskinfo[i][0],diskinfo[i][1],diskinfo[i][2])
        result.append(content)
    return result



def senddingtalk(content):
    token = '3a3c324bd12af1448a6934eeff387593234d047433bfc628574a8c1011050599'
    api = 'https://oapi.dingtalk.com/robot/send?access_token={}'.format(token)
    header = {'Content-Type': 'application/json'}
    data = {
        "msgtype": "text",
        "text": {

                  "content":content

        },
        'at': {
            'atMobiles': [
                '18370990913'

            ]
        },
        'isAtAll': 'false'
    }
    sendData = json.dumps(data).encode('utf-8')
    requests.post(url=api, data=sendData, headers=header)

def access_log(i,info,contents):
    path=os.listdir('./../')
    filename='access_log'
    for name in os.listdir('./../'):
        if fnmatch.fnmatch(name,filename):
            pass
        else:
            subprocess.run('touch ./../access_log',shell=True,stdout=subprocess.PIPE)
    with open(file='./../access_log',mode='a',encoding='utf8')as f:
        if 'cpuused' in contents:
            content='Date {} servername {} ERROR {} {}'.format(info[i][0],info[i][1],'cpuused',info[i][2])
        elif 'memoryused' in contents:
            content = 'Date {} servername {} ERROR {} {}'.format(info[i][0], info[i][1], 'memoryused', info[i][2])
        else:
            content = 'Date {} servername {} ERROR {} {}'.format(info[i][0], info[i][1], 'diskused', info[i][2])
        content=content+'\n'
        f.write(content)
        f.close()


# access_log()












