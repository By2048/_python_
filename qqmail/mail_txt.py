import smtplib

from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="1247079575@qq.com"    #用户名
mail_pass="ciaifqcjwtmmgahi"   #口令

from_usernaem = 'from_username-test'
from_address = '1247079575@qq.com'
to_username='to_username-test'
to_address = '2045516477@qq.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python 邮件发送测试...reervasvasv', 'plain', 'utf-8')
message['Subject'] = Header('Sub-Test', 'utf-8')  # 主题
message['From'] = Header(from_usernaem,'utf-8')
message['To'] = Header(to_username,'utf-8')


# msg.attach(MIMEText(str('Python测试内容'),'plain','utf-8'))
# msg.attach(MIMEText('<p><a href="http://www.baidu.com"></a></p>','html','utf-8'))


try:
    smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(from_address, to_address, message.as_string())
    smtpObj.quit()
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
    # ciaifqcjwtmmgahi