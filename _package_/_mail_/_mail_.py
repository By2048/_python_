import logging
import smtplib
from email.mime.text import MIMEText

# 阿里云邮件
MAIL_HOST = 'smtpdm.aliyun.com'
MAIL_PORT = 465
MAIL_USER = ''
MAIL_PWD = ''
FROM_ADDRESS = 'test@email.com'

DATA = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>title</title>
    <style>
        * {margin: 0;padding: 0}
        .logo {}
    </style>
</head>
<body>
    <div class="main">
        <header>
            <img src="" class="logo">
        </header>
        <div class="content">
            <h3></h3>  
            <p class="text">
            <b>{code}</b>
            <div class="tips">
                <p>本邮件由系统自动发送，请勿直接回复！</p>
            </div>
        </div>
    </div>
</body>
</html>"""


def send_mail(to_user, subject, code='xxx'):
    data = DATA.replace("{code}", code)
    msg = MIMEText(data, _subtype='html', _charset='utf-8')
    msg['Subject'] = subject
    msg['From'] = MAIL_USER
    msg['To'] = to_user
    try:
        server = smtplib.SMTP_SSL()
        server.connect(MAIL_HOST)
        server.login(MAIL_USER, MAIL_PWD)
        server.sendmail(MAIL_USER, to_user, msg.as_string())
        server.close()
        return True
    except Exception as error:
        logging.exception(f"发送邮件出错{error}")
        return False
