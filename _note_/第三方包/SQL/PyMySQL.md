pip install PyMySQL


#### 连接MySql数据库
```py
import pymysql  
  
# 打开数据库连接（ip/数据库用户名/登录密码/数据库名）  
db = pymysql.connect("localhost", "root", "admin", "test")  
# 使用 cursor() 方法创建一个游标对象 cursor  
cursor = db.cursor()  
  
# 使用 execute()  方法执行 SQL 查询  
cursor.execute("SELECT VERSION()")  
# 使用 fetchone() 方法获取单条数据.  
data = cursor.fetchone()  
print("Database version : %s " % data)  
  
# 关闭数据库连接  
db.close()
```



#### 操作MySql数据库实现增删改查

##### 插入
```py
import pymysql  
  
# 打开数据库连接（ip/数据库用户名/登录密码/数据库名）  
db = pymysql.connect("localhost", "root", "admin", "test")  
# 使用 cursor() 方法创建一个游标对象 cursor  
cursor = db.cursor()  
  
# SQL 插入语句
sql = """INSERT INTO user(name) 
         VALUES ('Mac')"""  
try:  
   # 执行sql语句  
   cursor.execute(sql)  
   # 提交到数据库执行  
   db.commit()  
except:  
   # 如果发生错误则回滚  
   db.rollback()  
  
# 关闭数据库连接  
db.close() 
```


##### 查询
```py
import pymysql  
  
# 打开数据库连接（ip/数据库用户名/登录密码/数据库名）  
db = pymysql.connect("localhost", "root", "root", "test")  
# 使用 cursor() 方法创建一个游标对象 cursor  
cursor = db.cursor()  
  
# SQL 查询语句  
sql = "SELECT * FROM user"  
  
try:  
    # 执行SQL语句  
    cursor.execute(sql)  
    # 获取所有记录列表  
    results = cursor.fetchall()  
    for row in results:  
        id = row[0]  
        name = row[1]  
        # 打印结果  
        print("id=%s,name=%s" % (id, name))  
except:  
    print("Error: unable to fecth data")  
  
# 关闭数据库连接  
db.close()  
```

##### 更新
```py
import pymysql  
  
# 打开数据库连接（ip/数据库用户名/登录密码/数据库名）  
db = pymysql.connect("localhost", "root", "root", "test")  
# 使用 cursor() 方法创建一个游标对象 cursor  
cursor = db.cursor()  
  
# SQL 更新语句  
sql = "UPDATE user SET name = 'Bob' WHERE id = 1"  
try:  
    # 执行SQL语句  
    cursor.execute(sql)  
    # 提交到数据库执行  
    db.commit()  
except:  
    # 发生错误时回滚  
    db.rollback()  
     
# 关闭数据库连接  
db.close()  
```


##### 删除
```py
import pymysql  
  
# 打开数据库连接（ip/数据库用户名/登录密码/数据库名）  
db = pymysql.connect("localhost", "root", "root", "test")  
# 使用 cursor() 方法创建一个游标对象 cursor  
cursor = db.cursor()  
  
# SQL 删除语句  
sql = "DELETE FROM user WHERE id  = 1"  
try:  
    # 执行SQL语句  
    cursor.execute(sql)  
    # 提交修改  
    db.commit()  
except:  
    # 发生错误时回滚  
    db.rollback()  
  
# 关闭数据库连接  
db.close()  

```