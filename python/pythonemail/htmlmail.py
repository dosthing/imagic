#!/usr/bin/python3
 
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
 
my_sender='your163email@163.com'    
my_pass = 'yourpassword'            # 邮箱登录授权码
my_user='1213334346@qq.com'      
def mail():
    ret=True
    try:
        msg=MIMEText('dosthing','plain','utf-8')
        msg['From']=formataddr(["dosthing",my_sender])  
        msg['To']=formataddr(["FK",my_user])             
        msg['Subject']="来自2019的最亲切的问候by dosting！"             
 
        server=smtplib.SMTP_SSL("smtp.163.com", 465)  
        server.login(my_sender, my_pass)  
        server.sendmail(my_sender,[my_user,],msg.as_string())  
        server.quit()  
    except Exception:  
        ret=False
    return ret
 
ret=mail()
if ret:
    print("send success")
else:
    print("send fail")