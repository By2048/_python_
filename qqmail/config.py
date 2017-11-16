import json
import os

qq_mail_json_path = r'E:\Desktop\qq_mail_config.json'

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器

from_title = 'from_title'
to_title = 'to_title'

from_address = '1247079575@qq.com'
to_address = '2045516477@qq.com'  # 接收邮件的邮箱


# 保险起见使用设置文件读取本机的邮箱配置
# 配置格式如下
# {
#     "mail_user": "1247079575@qq.com",
#     "mail_pass": "ciaif------ahi"
# }
def get_config():
    file = open(qq_mail_json_path, 'rb')
    json_info = json.load(file)
    mail_user = json_info["mail_user"]
    mail_pass = json_info["mail_pass"]
    return mail_user, mail_pass


mail_user, mail_pass = get_config()
