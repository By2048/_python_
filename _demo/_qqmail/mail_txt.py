import smtplib

from email.mime.text import MIMEText
from email.header import Header

try:
    from config import *
except ImportError:
    from .config import *


# msg.attach(MIMEText(str('Python测试内容'),'plain','utf-8'))
# msg.attach(MIMEText('<p><a href="http://www.baidu.com"></a></p>','html','utf-8'))



# 发送邮件 txt_info 到 to_email
# to_address 发送到的邮箱
# 发件人：from_title
# 收件人：to_title
# topic 邮件主题
def mail_txt(txt_info, to_address=to_address,from_title=from_title, to_title=to_title,topic='mail_topic'):
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(txt_info, 'plain', 'utf-8')
    message['Subject'] = Header(topic, 'utf-8')  # 主题
    message['From'] = Header(from_title, 'utf-8')
    message['To'] = Header(to_title, 'utf-8')
    try:
        smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(from_address, to_address, message.as_string())
        smtpObj.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


if __name__ == '__main__':
    mail_txt('rwerwerew---==-=-=-=--=-=')
    # pass
