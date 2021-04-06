import smtplib
from email.mime.text import MIMEText
from email.header import Header

from _conf_._config_ import QQMAIL_HOST, QQMAIL_PORT, QQMAIL_USER, QQMAIL_PASSWORD

try:
    from loguru import logger
except ImportError:
    class logger(object):
        info = print
        error = print
        exception = print


#        信息 : data
# 发送到的邮箱 : to_address
#       发件人： from_title
#       收件人： to_title
#     邮件主题 : subject

def mail_txt(data, to_address, from_title, to_title, subject):
    message = MIMEText(data, 'plain', 'utf-8')

    message['Subject'] = Header(subject, 'utf-8')
    message['From'] = Header(from_title, 'utf-8')
    message['To'] = Header(to_title, 'utf-8')

    try:
        smt = smtplib.SMTP_SSL(QQMAIL_HOST, 465)
        smt.login(QQMAIL_USER, QQMAIL_PASSWORD)
        smt.sendmail(QQMAIL_USER, to_address, message.as_string())
        logger.info("邮件发送成功")
        smt.quit()
    except Exception as e:
        logger.error("Error: 无法发送邮件")
        logger.exception(e)


if __name__ == '__main__':
    mail_txt(
        "TestTextContent",
        to_address='byamend@gmail.com',
        from_title='from_title',
        to_title='to_title',
        subject='mail_subject'
    )
