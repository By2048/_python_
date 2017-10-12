import requests
from bs4 import BeautifulSoup


login_header = {
    'Host': 'acm.usx.edu.cn',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://acm.usx.edu.cn/AspNet/Status.aspx?status=100',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '635',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests':'1'
}
login_data={
    'ctl00$LoginView$Login1$UserName':'usx14305',
    'ctl00$LoginView$Login1$Password':'cmeng',
    'ctl00$LoginView$Login1$LoginButton':'Login',
    '_VIEWSTATE':'/wEPDwULLTE0Njk0ODUxMjNkZDE3Terz2CiL41rmQXKBL7NjAtJo',
    '__VIEWSTATEGENERATOR':'EAE6C16D'
}
ques_header = {
    'Host': 'acm.usx.edu.cn',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://acm.usx.edu.cn/AspNet/Status.aspx?status=100',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '635',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests':'1'
}

cookie='M_distinctid=15ef5fc5ae79c0-0a41af196fd656-c303767-15f900-15ef5fc5ae88ef; CNZZDATA5302147=cnzz_eid%3D804732002-1507361058-http%253A%252F%252Facm.usx.edu.cn%252F%26ntime%3D1507361058; .aspxlogin=87F7B498F4D62B8FD13FDDF299C3B913DA131038F6F2E00AA57D0CB03718CAF07266EC7BB33A3D4BFE7911AFEB419D40AD45B0BC0CEF3B5FA1C4BE67937ABF9EB1B290780A81E94C767846A94BFF5CAF5F3C3F9AB0242AC689C76CED7A7BB506A9919DD6610E2B431F9664187C4A12B22A2C2479'

cookies={
    '.aspxlogin':'39F778891ADA20102335E0BD4D050D611C52433FC4204C0FAA90CDE5BF4DECD737FCD3BA28D7C677F1EF1F848F6883E5CE25D0B5DBA5EF8E1B9A7675294EC4B52460DF61483FC83B78631E6103837A36F7318C5E37DC542B9E5701B35E16F9D942F2DE3FABE35B6C00B694D2B7B60AA04F667E48',
    'CNZZDATA5302147':'cnzz_eid%3D804732002-1507361058-http%253A%252F%252Facm.usx.edu.cn%252F%26ntime%3D1507361058',
    'UM_distinctid':'15ef5fc5ae79c0-0a41af196fd656-c303767-15f900-15ef5fc5ae88ef'
}





login_session = requests.Session()
login_session.post(url='http://acm.usx.edu.cn/AspNet/Default.aspx', data=login_data,headers=login_header)

po=login_session.get('http://acm.usx.edu.cn/AspNet/Status.aspx?status=100')
soup=BeautifulSoup(po.text,'html.parser')
print(soup)



code_link='http://acm.usx.edu.cn/AspNet/Submit.aspx?qid=1000'
code_header={
    'Host': 'acm.usx.edu.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://acm.usx.edu.cn/AspNet/Submit.aspx?qid=1000',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'UM_distinctid=15ef5fc5ae79c0-0a41af196fd656-c303767-15f900-15ef5fc5ae88ef; CNZZDATA5302147=cnzz_eid%3D804732002-1507361058-http%253A%252F%252Facm.usx.edu.cn%252F%26ntime%3D1507361058; .aspxlogin=39F778891ADA20102335E0BD4D050D611C52433FC4204C0FAA90CDE5BF4DECD737FCD3BA28D7C677F1EF1F848F6883E5CE25D0B5DBA5EF8E1B9A7675294EC4B52460DF61483FC83B78631E6103837A36F7318C5E37DC542B9E5701B35E16F9D942F2DE3FABE35B6C00B694D2B7B60AA04F667E48',
    'Content-Length': '635',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests':'1'
}
code_date={
    '__EVENTTARGET'	:'ctl00$Content$Button1',
    '__EVENTARGUMENT':'',
    '__VIEWSTATE':'/wEPDwUJNzQ4MTE3NzAxZBgCBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAgUXY3RsMDAkTG9naW5TdGF0dXMkY3RsMDEFF2N0bDAwJExvZ2luU3RhdHVzJGN0bDAzBQ9jdGwwMCRMb2dpblZpZXcPD2QCAWSpd562hsZ+3Wq7IgwLpU3sltMhCw==',
    '__VIEWSTATEGENERATOR':'52830EE0',
    '__EVENTVALIDATION':'/wEWDAKhorzhAwL497TjBgKW7ZnfDgL4l+6kAQKj0flcAonfq0UCoYCOoAICr63u+QQCzfWC3gwCq/HPsAQCl46S8AkCv6XXqw2b68i1d5n7awRuxCy+DbR4MyA7yQ==',
    'ctl00$Content$username':'usx14305',
    'ctl00$Content$Num':'1000',
    'ctl00$Content$DropDownList1':'cpp',
    'ctl00$Content$TextBox1':'210.33.26.200',
    'ctl00$Content$TCode':'111111111111111111112222222222222222222'
}
code_date_1={
    'ctl00$Content$username': 'usx14305',
    'ctl00$Content$Num': '1000',
    'ctl00$Content$DropDownList1': 'cpp',
    'ctl00$Content$TextBox1': '210.33.26.200',
    'ctl00$Content$TCode': '111111111111111111112222222222222222222'
}

# login_session.='''UM_distinctid=15ef5fc5ae79c0-0a41af196fd656-c303767-15f900-15ef5fc5ae88ef; CNZZDATA5302147=cnzz_eid%3D804732002-1507361058-http%253A%252F%252Facm.usx.edu.cn%252F%26ntime%3D1507361058; .aspxlogin=87F7B498F4D62B8FD13FDDF299C3B913DA131038F6F2E00AA57D0CB03718CAF07266EC7BB33A3D4BFE7911AFEB419D40AD45B0BC0CEF3B5FA1C4BE67937ABF9EB1B290780A81E94C767846A94BFF5CAF5F3C3F9AB0242AC689C76CED7A7BB506A9919DD6610E2B431F9664187C4A12B22A2C2479; ASP.NET_SessionId=luzp5kf5ukqjz0izb1vdim55'''

requests.utils.add_dict_to_cookiejar()

print(login_session.cookies)

login_session.post(url=code_link,data=code_date_1,headers=code_header)

print('----')
