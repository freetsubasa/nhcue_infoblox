#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-
import os, sys
from radius import RADIUS

USER, PASSWD = (sys.argv[1], sys.argv[2]) if len(sys.argv) > 2 else ('account', 'password')

host = 'IP'
port = 1812
secret = 'KEY'

r = RADIUS(secret,host,port)

r.timeout = 10

if r.authenticate(USER,PASSWD):
    print "Authentication Succeeded"
else:
    print "Authentication Failed"
