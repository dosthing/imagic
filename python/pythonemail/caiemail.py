#!/usr/bin/python3
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import email.mime.multipart
import email.mime.text
 
sender = '18578776389@163.com'
receivers = ['1213334346@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
#message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
#message['From'] = Header("菜鸟教程", 'utf-8')     # 发送者
#message['To'] =  Header("测试", 'utf-8')          # 接收者
 
#subject = 'Python SMTP 邮件测试'
#message['Subject'] = Header(subject, 'utf-8')
msg = email.mime.multipart.MIMEMultipart()
msg['from'] = '18578776389@163.com'
msg['to'] = '1213334346@qq.com'
msg['subject'] = 'test，这是邮件主题'
content = 'python email'
'''''
    你好，
            这是一封自动发送的邮件的内容。
'''
txt = email.mime.text.MIMEText(content)
msg.attach(txt)
 
 
try:
    smtpObj = smtplib
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.connect('smtp.163.com') # 使用的发送者邮箱的那啥来着，post
    print ('connect')
    smtpObj.login('18578776389@163.com', 'li60207')
    print ('login')
    smtpObj.sendmail(sender, receivers,str(msg))# message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")
