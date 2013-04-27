#!/usr/bin/python
# -*- coding: utf-8 -*-

from subprocess import call
from datetime import datetime

logfile="checksys.log"
Flog=open(logfile,"a")

def w():
    """ 谁当前登入了系统 """
    #call(["w"])
    call(["w"],stdout=Flog)

def last():
    """ 最后登入系统的日志信息 """
    call(["last","-n 10"],stdout=Flog)

commandlist={
    "w":["w"],
    "last":["last","-n","10"],
    #当前登入了系统,最后登入系统的日志信息
    "history":["history","20"],
    #查看当前系统最后20条命令
    "ps":["ps","aux"],
    "pstree":["pstree","-a"],
    #什么程序在运行,显示进程树
    "netstat":["netstat","-nuxtlp"],
    #当前系统监听的服务
    "free":["free","-m"],
    "top":["top","-n","1"],
    #显示cpu和mem资源
    "lspci":["lspci"],
    "dmidecode":["dmidecode"],
    #硬件相关信息
    "iostat":["iostat","-kx","2"],
    "vmstat":["vmstat","2","10"],
    "mpstat":["mpstat","2","10"],
    "dstat":["dstat","--top-io","--top-bio"],
    #磁盘IO性能
    "mount":["mount"],
    "df":["df","-h"],
    #挂载点和文件系统
    "sysctl":["sysctl","-a"],
    "interrupts":["cat","/proc/interrupts"],
    "ip_conntrack":["cat","/proc/net/ip_conntrack"],
    "ss":["ss","-s"]
    #kernel参数，中断

    }
b=commandlist['w']
#print b
#print datetime.now()
#Flog.write(str(datetime.now()))
def command(c):
    Flog.write(str(datetime.now())+"\n")
    Flog.flush()
    call(c,stdout=Flog)

command(b)
