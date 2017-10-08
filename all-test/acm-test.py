import requests
conn = requests.session()

link='http://acm.usx.edu.cn/AspNet/Default.aspx'

resp = conn.get(link)
# 打印请求的头
print(resp.request.headers)
# 打印结果如下，requests已经自动填充了部分数据

resp = conn.get(link)
print(resp.request.headers)
print(resp.cookies.items())