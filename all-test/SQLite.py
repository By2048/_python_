import sqlite3

cx = sqlite3.connect("F:\\_Test\\test.db")

cu=cx.cursor()

# cu.execute("create table catalog (id integer primary key,pid integer,name varchar(10) UNIQUE,nickname text NULL)")


# for t in[(0,10,'abc','Yu'),(1,20,'cba','Xu')]:
#     cx.execute("insert into catalog values (?,?,?,?)", t)
#
# cx.commit()

#
# cu.execute("select * from catalog")
#
# print(cu.fetchone())
# print(cu.fetchone())

# cu.execute("update catalog set name='Boy' where id = 0")
# cx.commit()

# x=u'鱼'
# cu.execute("update catalog set name=? where id = 0",x)
# cu.execute("select * from catalog")
# print(cu.fetchall())
# [(0, 10, u'\u9c7c', u'Yu'), (1, 20, u'cba', u'Xu')]


# for item in cu.fetchall():
#     for element in item:
#         print(element)
#     print('\n')

cx.row_factory = sqlite3.Row
c = cx.cursor()
c.execute('select * from catalog')

r = c.fetchone()
print(type(r))  # <class 'sqlite3.Row'>

print(r)  # <sqlite3.Row object at 0x02F16AB0>

for p in r:
    print(p)    # 0 10 鱼 Yu

print(len(r))   # 4

print(r[2]) # 鱼

print(r.keys()) # ['id', 'pid', 'name', 'nickname']

print(r['id'])  # 0
