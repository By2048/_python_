import pymysql
import os
import time
from PIL import Image


# 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
con_text = pymysql.connect(host="localhost", user="root", passwd="admin", db="bing",use_unicode = True,charset ="utf8")
# 使用 cursor() 方法创建一个游标对象 cursor

cursor = con_text.cursor()

rootDir = "F:\Image\Bing"


# 图片信息(Img)
class Img:
    Name = ""
    Path = ""
    Type = ""
    Size = ""  # 图片大小
    Width = ""
    Height = ""
    ShowDate=""     # 文件显示时的时间
    VisitDate = ""  # 文件最后访问时间
    CreateDate = ""  # 文件创建时间
    ChangeDate = ""  # 文件最后修改时间

    def __init__(self,  name, path, type, size, width, heigth, showDate, visitDate, createDate, changeDate):
        self.Name = name
        self.Path = path
        self.Type = type
        self.Size = size
        self.Width = width
        self.Height = heigth
        self.ShowDate=showDate
        self.VisitDate = visitDate
        self.CreateDate = createDate
        self.ChangeDate = changeDate

# 图片信息插入数据库
def insert_sql(img):
    insert = "insert into Images (Name,Path,Type,Size,Width,Height,ShowDate,VisitDate,CreateDate,ChangeDate)"
    values = "values ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}','{9}')" \
        .format(img.Name, img.Path, img.Type, img.Size, img.Width, img.Height,img.ShowDate, img.VisitDate,img.CreateDate, img.ChangeDate)
    insert_sql = insert + '\n' + values
    sql_cursor = con_text.cursor()
    sql_cursor.execute(insert_sql)
    con_text.commit()


# 获取图片文件具体信息
def get_image_info(path):
    name = os.path.basename(path)
    type = os.path.splitext(path)[1].replace(".", "")
    size = int(os.path.getsize(path) / 1024)
    atime = os.path.getatime(path)  # 文件最后访问时间
    ctime = os.path.getctime(path)  # 文件创建时间
    mtime = os.path.getmtime(path)  # 文件最后修改时间
    _atime = time.localtime(atime)
    _ctime = time.localtime(ctime)
    _mtime = time.localtime(mtime)
    showDate=name[0:10]
    visit_date = str(_atime[0]) + "-" + str(_atime[1]) + "-" + str(_atime[2]) + " " + \
                 str(_atime[3]) + ":" + str(_atime[4]) + ":" + str(_atime[5])
    create_date = str(_ctime[0]) + "-" + str(_ctime[1]) + "-" + str(_ctime[2]) + " " + \
                  str(_ctime[3]) + ":" + str(_ctime[4]) + ":" + str(_ctime[5])
    change_date = str(_mtime[0]) + "-" + str(_mtime[1]) + "-" + str(_mtime[2]) + " " + \
                  str(_mtime[3]) + ":" + str(_mtime[4]) + ":" + str(_mtime[5])
    width = Image.open(path).size[0]
    height = Image.open(path).size[1]
    return Img(name, path, type, size, width, height,showDate, visit_date, create_date, change_date)

def init_sql():
    for file_name in os.listdir(rootDir):
        if file_name=='-Temp.jpg':
            pass
        else:
            path = os.path.join(rootDir, file_name)
            img_info=get_image_info(path)
            insert_sql(img_info)

if __name__=='__main__':
    # print('\n'.join(os.listdir(rootDir)))
    init_sql()

    # # 使用 execute()  方法执行 SQL 查询
    # cursor.execute("SELECT VERSION()")
    # # 使用 fetchone() 方法获取单条数据.
    # data = cursor.fetchone()
    # print("Database version : %s " % data)