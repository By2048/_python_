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
keep_path = r'F:\Image\mzitu'


has_down_txt_path = r'E:\MyGit\Python\reptile\mzitu\has_down.txt'

has_down_sql_path = r'E:\MyGit\Python\reptile\mzitu\download.db'


# 浏览器标识
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/53.0.2785.143 Safari/537.36'
headers = {'User-Agent': user_agent}

all_img_page_link = 'http://www.mzitu.com/all'
start_page_link = 'http://www.mzitu.com'

sql_server_con_text = pyodbc.connect('DRIVER={SQL Server};SERVER=.;DATABASE=Mzitu;UID=mzitu;PWD=password')

mysql_con_text = pymysql.connect(host="localhost", user="root", passwd="admin",
                                 db="mzitu", use_unicode=True, charset="utf8")
