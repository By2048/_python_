# -*- coding: utf-8 -*-

import pyodbc

# 连接字符串
con_text = pyodbc.connect('DRIVER={SQL Server};SERVER=.;DATABASE=ImageWebSite;UID=image-link;PWD=P@ssw0rd')

# 使用 conn_text 创建一个游标
sql_cursor = con_text.cursor()
sql_cursor.execute("select * from ImgFolderInfo")

# row = sql_cursor.fetchone()
# print('name:', row[1])
# print('name:', row.Name)

# for row in sql_cursor:
#     print(row.Id, row.Name)

# for row in sql_cursor.execute("select * from ImgFolderInfo"):
#     print(row.Id,row.Name)

# rows = sql_cursor.fetchall()
# for row in rows:
#     print(row.Id,row.Name)


#
sql_cursor.execute("insert into ImgFolderInfo(Name)"
                   "values ('{name}')".format(name="13112321323"))
con_text.commit()

# deleted = sql_cursor.execute("delete from ImgFolderInfo where id = '4'").rowcount
# con_text.commit()
# print(deleted)
