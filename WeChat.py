'''微信自动发消息'''

import itchat
import time
import sys

i = 0
itchat.auto_login() #//登录微信
#login = itchat.auto_login()

#content = "您好，这里是4091机器人帝国，请无视这条消息"
while 1:
    try:
        Name = str(input("请输入目标微信昵称："))
        author = itchat.search_friends(nickName = Name)[0]
    except IndexError:
        print("抱歉，查找不到此用户。"+'\n')
    else:
        Input_content = str(input ("输入发送的内容："))
        s = int(input("请输入每隔几秒钟发一条消息："))
        while True:
            content = Input_content
            content = "*"*i+content+"*"*i
            author.send(content)
            print(str(i)+"次循环："+content+'\n'+'已发送成功'+'\n')
            time.sleep(s)
            i = i+1
