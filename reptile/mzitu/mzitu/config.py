import socket
import multiprocessing
import pyodbc
import pymysql

# 超时等待时间
wait_time = 10
socket.setdefaulttimeout(wait_time)

# 进程池数量
pool_num = multiprocessing.cpu_count() * 3

# 下载路径
keep_path = "F:\\Image\\mzitu\\"

# 已经下载的文件路径
# 使用绝对目录
has_down_path=r'E:\Desktop\Python\reptile\mzitu\has_down.txt'

# 使用mziti.py使用
# has_down_path = "../has_down.txt"

# 使用setup.py使用
# has_down_path = "has_down.txt"

# 浏览器标识
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
headers = {'User-Agent': user_agent}

all_img_page = 'http://www.mzitu.com/all'
start_page = 'http://www.mzitu.com'

sql_server_con_text = pyodbc.connect('DRIVER={SQL Server};SERVER=.;DATABASE=Mzitu;UID=mzitu;PWD=password')

mysql_con_text = pymysql.connect(host="localhost", user="root", passwd="admin", db="mzitu", use_unicode=True,
                                 charset="utf8")
