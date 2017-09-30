from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib
import os

# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="1247079575@qq.com"    #用户名
mail_pass="ciaifqcjwtmmgahi"   #口令

from_usernaem = 'from_username-test'
from_address = '1247079575@qq.com'
to_username='to_username-test'
to_address = '2045516477@qq.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱


def send_image_mail(img_path):
    message = MIMEMultipart()
    mail_body = MIMEText('Test-Image，\n附件的邮件。', 'plain', 'utf-8')
    message.attach(mail_body)
    message['Subject'] = Header('Sub-Test-Head', 'utf-8')  # 主题
    message['From'] = Header(from_usernaem, 'utf-8')
    message['To'] = Header(to_username, 'utf-8')
    baseName = os.path.basename(img_path)
    att = MIMEApplication(open(img_path, 'rb').read())
    att.add_header('Content-Disposition', 'attachment', filename=baseName)
    message.attach(att)
    try:
        smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(from_address, to_address, message.as_string())
        smtpObj.quit()
        print("发送邮件成功")
    except smtplib.SMTPException:
        print("Error: 发送邮件失败")

if __name__=='__main__':
    filePath = 'F:\\008.jpg'
    send_image_mail(filePath)
