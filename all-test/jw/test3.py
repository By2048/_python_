import requests

SecretCode=input('验证码')

data = {
    '__VIEWSTATE': 'dDwyODE2NTM0OTg7Oz76KAIzEOLDS5fWN9NIrqLdruD9ag==',
    'txtUserName': '用户名',
    'TextBox2': '密码',
    'txtSecretCode': SecretCode,
    'RadioButtonList1': '学生',
    'Button1': '',
    'lbLanguage': '',
    'hidPdrs': '',
    'hidsc': ''
}


code='http://jw.usx.edu.cn/CheckCode.aspx'

picture=requests.get(code)
# 保存验证码到本地
local = open('image-test.html', 'wb')
local.write(picture.read)

