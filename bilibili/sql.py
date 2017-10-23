import pymysql

try:
    from config import *
except ImportError:
    from .config import *

def insert_image(img):
    insert="insert into image(name,author,down_link,num,upload_time,tag,md5,character_name,source_anime,discription)"
    values="values ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}','{9}')"\
        .format(img.name,img.author,img.down_link,img.num,img.upload_time,img.tag,img.md5,img.character_name,img.source_anime,img.discriptionimg)
    insert_sql = insert + '\n' + values
    sql_cursor = db.cursor()
    try:
        sql_cursor.execute(insert_sql)
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()


def get_img_id(md5):
    data=None
    try:
        search_sql = "select id from image where md5='{0}'".format(md5)
        cursor = db.cursor()
        cursor.execute(search_sql)
        data = cursor.fetchone()
    except:
        pass
    return data[0]

