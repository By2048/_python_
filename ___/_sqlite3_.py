#

import sqlite3

# 在调用connect函数的时候，指定库名称
# 如果指定的数据库存在就直接打开这个数据 库
# 如果不存在就新创建一个再打开。
conn = sqlite3.connect("E:/test.db")

# 也可以创建数据库在内存中。
conn = sqlite3.connect(":memory:")

# 打开数据库时返回的对象cx就是一个数据库连接对象，它可以有以下操作：
# commit()--事务提交
# rollback()--事务回滚
# close()--关闭一个数据库连接
# cursor()--创建一个游标
# 关于commit()，如果isolation_level隔离级别默认，那么每次对数据库的操作，都需要使用该命令，你也可
# 以设置isolation_level=None，这样就变为自动提交模式。
# 使用游标对象SQL语句查询数据库，获得查询对象
cur = conn.cursor()

# 游标对象有以下的操作：
# execute()--执行sql语句
# executemany--执行多条sql语句
# close()--关闭游标
# fetchone()--从结果中取一条记录，并将游标指向下一条记录
# fetchmany()--从结果中取多条记录
# fetchall()--从结果中取出所有记录
# scroll()--游标滚动


# 插入数据库
for item in [(0, 10, 'abc', 'Yu'), (1, 20, 'cba', 'Xu')]:
    cur.execute("insert into catalog values (?,?,?,?)", item)

# 简单的插入两行数据
# 只有提交了之后,才能生效.我们使用数据库连接对象cx来进行提交commit和回滚rollback操作.
conn.commit()

# 查询
cur.execute("select * from catalog")
print(cur.fetchall())  # [(0, 10, u'\u9c7c', u'Yu'), (1, 20, u'cba', u'Xu')]

# 如果我们使用cu.fetchone(),则首先返回列表中的第一项,再次使用,则返回第二项,依次下去.
cur.execute('select * from catalog')
print(cur.fetchone())  # (0, 10, 'Boy', 'Yu')
print(cur.fetchone())  # (1, 20, 'cba', 'Xu')

# 修改
cur.execute("update catalog set name='Boy' where id = 0")
conn.commit()

# 使用中文 先确定你的IDE或者系统默认编码是utf-8,并且在中文前加上u
x = u'鱼'
cur.execute("update catalog set name=? where id = 0", x)
cur.execute("select * from catalog")
print(cu.fetchall())  # [(0, 10, '鱼', 'Yu'), (1, 20, 'cba', 'Xu')]

# 如果要显示出中文字体，那需要依次打印出每个字符串

for item in cur.fetchall():
    for element in item:
        print(element)
    print('\n')
    # 0
    # 10
    # 鱼
    # Yu
    #
    # 1
    # 20
    # cba
    # Xu

    cx.row_factory = sqlite3.Row
    c = cx.cursor()
    c.execute('select * from catalog')

    r = c.fetchone()
    print(type(r))  # <class 'sqlite3.Row'>

    print(r)  # <sqlite3.Row object at 0x02F16AB0>

    for item in r:
        print(item)  # 0 10 鱼 Yu

    print(len(r))  # 4

    print(r[2])  # 鱼

    print(r.keys())  # ['id', 'pid', 'name', 'nickname']

    print(r['id'])  # 0
