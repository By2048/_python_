import pymysql

try:
    from config import *
    from tool import *
except ImportError:
    from .config import *
    from .tool import *


def insert_bili_img(img):
    name=repr(list_to_string(img.name))
    down_link=repr(list_to_string(img.down_link))
    author=repr(img.author)
    detail_link=repr(img.detail_link)
    num=repr(img.num)
    create_date=repr(img.create_date)
    category=repr(list_to_string(img.category))
    tag=repr(list_to_string(img.tag))
    character_name=repr(list_to_string(img.character_name))
    source=repr(list_to_string(img.source))
    discription=repr(img.discription)

    insert="insert into image(name,down_link,author,detail_link,num,create_date,category,tag,character_name,source,discription)"
    values="values ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8},{9},{10});"\
        .format(name,down_link,author,detail_link,num,create_date,category,tag,character_name,source,discription)
    insert_sql = insert + values
    print(insert_sql,end='\n\n')
    sql_cursor = db.cursor()
    sql_cursor.execute(insert_sql)
    db.commit()
    # except:
        # 发生错误时回滚
        # db.rollback()

def get_img_id_by_name(name):
    data=None
    try:
        search_sql = "select id from image where name='{0}'".format(name)
        cursor = db.cursor()
        cursor.execute(search_sql)
        data = cursor.fetchone()
    except:
        pass
    return data[0]
