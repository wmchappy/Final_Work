#!/usr/bin/python
#vim: set fileencoding:utf-8

import werobot
robot = werobot.WeRoBot(token='tokenhere')  #token="tokenhere"
@robot.text
def echo(message):
    a = '<a href=\'http://class.710071.net?wechatid=\".$fromUsername.\"\'>点击进入西电微信课堂</a>'
    if message.content ==  "hello" :
        return a 
    else:
        return '请输入hello'
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
