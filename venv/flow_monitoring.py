import os
from datetime import time
from typing import re


def getIe(packages = ""):
    #获取应用的uid
    uid = os.popen('adb shell "dumpsys package ' + packages + ' | grep userId="').readline()
    uid = uid[re.search("userId=",uid).span()[1]:].split(" ")[0]
    internet = {}
    rec = 0
    send = 0
    #获取应用的流量数据
    flow = os.popen('adb shell "cat /proc/net/xt_qtaguid/stats | grep '+uid+'"').readlines()
    #统计所有wlan0的发送、接收流量单位为KB
    for i in flow:
        if "wlan0" in i:
            rec += int(i.split(" ")[5])/1024
            send += int(i.split(" ")[7])/1024
            internet["rec:"] = rec
            internet["send:"] = send
            internet["time:"] = time.time()
            return internet