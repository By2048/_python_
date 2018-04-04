import pymysql

mysql_con_text = pymysql.connect(host="localhost",
                                 user="root",
                                 passwd="mysql_password",
                                 db="test",
                                 use_unicode=True,
                                 charset="utf8")


def init_table():
    init_sql = '''create table if not exists `user` (
`id` int auto_increment,
`name` varchar(20) not null,
primary key( `id` )
) engine=innodb default charset=utf8;'''
    sql_cursor = mysql_con_text.cursor()
    sql_cursor.execute(init_sql)
    mysql_con_text.commit()


def insert_sql():
    for i in range(1000):
        insert_sql = "insert into user(name) values ('{0}')".format('name_' + str(i))
        print(insert_sql)
        sql_cursor = mysql_con_text.cursor()
        sql_cursor.execute(insert_sql)
        mysql_con_text.commit()


# INSERT INTO user(name) VALUES ('name_0')


init_table()


insert_sql()
