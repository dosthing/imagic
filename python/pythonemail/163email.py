#!/usr/bin/python3
 
import smtplib
import email.mime.multipart
import email.mime.text

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

smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com') # 使用的发送者邮箱的那啥来着，post
smtp.login('18578776389@163.com', 'li60207')
smtp.sendmail('18578776389@163.com', '1213334346@qq.com', str(msg))
smtp.quit()