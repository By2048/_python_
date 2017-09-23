import os

rootDir = "F:\\Image\\mzitu\\车模易欣火爆身段袭人眼球 撩人姿势与兰博基尼激情缠绵"

for root, dirs, files in os.walk(rootDir):
    # print(root)
    # print(dirs)
    print(files)
    print(root)

pp="FImage\\mzitu\\上围摇摇欲坠性感女主播夏美酱晒性感新照超大胸器撑爆屏幕\\05a01.jpeg"

print(pp.split('\\')[-1])


# import pymysql
#
# # 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
# db = pymysql.connect(host="localhost", user="root", passwd="admin", db="mzitu",use_unicode = True,charset ="utf8")
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# # # 使用 execute()  方法执行 SQL 查询
# # cursor.execute("SELECT VERSION()")
# # # 使用 fetchone() 方法获取单条数据.
# # data = cursor.fetchone()
# # print("Database version : %s " % data)
#
# user_str='''INSERT INTO Users(UserName,ActualName,Sex,Age,Birthday,PassWord,Email,UserType,Balance,BorrowNum,CreateDate,Information)
# VALUES('A001','user-1','男','20','2011-11-11','123','123@123.123','vip-1','100','0','2015-11-5 21:21:25 ','user-Info')
# '''
#
#
#
# cursor.execute(user_str)
#
# db.commit()
#
# # 关闭数据库连接
# db.close()

