#！/bin/bash

import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_mail(email_content):
    mail_host="smtp.exmail.qq.com"
    mail_user="watchdog@thorough.ai"
    mail_pass="Xueqing1101"

    sender = 'watchdog@thorough.ai'
    receivers = ['wangyuxi@thorough.ai']
    content = email_content

    message = MIMEText(content, 'html', 'utf-8')
    message['From'] = Header("WatchDog", 'utf-8')
    message['To'] =  Header("系统管理人员", 'utf-8')

    subject = u'这是一个测试'
    message['Subject'] = Header(subject, 'utf-8')

    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())

send_mail('CPU报错')
