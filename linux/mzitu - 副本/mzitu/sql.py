import sqlite3
import os


from config import *


def init_sql():
    create_has_down = """create table has_down
    (
        id         integer  not null,
        link       text     not null,
        title      text     not null,
        category   text     not null,
        date       text     not null
    );"""
    create_error_down = """create table error_down
    (
        id         integer primary key,
        link       text     not null,
        title      text     not null
    );"""
    con = sqlite3.connect(has_down_sql_path)
    cur = con.cursor()
    cur.execute(create_has_down)
    cur.execute(create_error_down)
    con.commit()
    con.close()


def clear_sql():
    con = sqlite3.connect(has_down_sql_path)
    cur = con.cursor()
    cur.execute('DELETE FROM has_down')
    cur.execute('DELETE FROM error_down')
    con.commit()
    con.close()


def insert_to_has_down(meizi):
    con = sqlite3.connect(has_down_sql_path)
    cur = con.cursor()
    cur.execute("insert into has_down (id,link,title,category,date) values ('{0}','{1}','{2}','{3}','{4}')"
                .format(meizi.id, meizi.link, meizi.title, meizi.category, meizi.date))
    con.commit()
    con.close()


def get_all_has_down():
    conn = sqlite3.connect(has_down_sql_path)
    cur = conn.cursor()
    cur.execute("SELECT link FROM has_down")
    has_down = []
    for item in cur.fetchall():
        has_down.append(item[0])
    return has_down


def insert_to_error_down(meizi):
    con = sqlite3.connect(has_down_sql_path)
    cur = con.cursor()
    cur.execute("insert into error_down (link,title) values ('{0}','{1}')"
                .format(meizi.link, meizi.title))
    con.commit()
    con.close()


def get_all_error_down():
    pass


if __name__ == '__main__':
    has_down = get_all_has_down()
    error_down = get_all_error_down()
    # clear_sql()
