#!/usr/bin/python
# -*- coding: utf-8 -*-

from subprocess import call

logfile="checksys.log"
Flog=open(logfile,"w+")

def w():
    """ 谁当前登入了系统 """
    #call(["w"])
    call(["w"],stdout=Flog)

def last():
    """ 最后登入系统的日志信息 """
    call(["last","-n 10"],stdout=Flog)

a={"w":["w"],
   "last":["last","-n","10"]
        }
b=a['w']
print b
def command(c):
    call(c,stdout=Flog)

command(b)
