import sqlite3

sql_path = 'T:\\_tmp\\image.db'

# sql_path = '/home/python/wallpaper/image.db'



def init_sql():
    create_category = """create table category
    (
        id     integer   not null,
        name   text      not null,
        count  integer   
    );"""

    create_image = """create table image
    (
        image_id        integer   ,
        image_name      text      ,
        category_id     integer   ,
        image_url       text      ,
        image_url_thumb text      ,
        width           integer   ,
        height          integer   ,
        file_type       text      ,
        file_size       integer   ,
        tags            text      
    );"""

    create_tag = """create table tag
    (
        id      integer   not null,
        name    text      not null,
        count   integer   
    );"""

    con = sqlite3.connect(sql_path)
    cur = con.cursor()
    cur.execute(create_category)
    cur.execute(create_tag)
    cur.execute(create_image)
    con.commit()
    con.close()


def insert_category(categorys):
    con = sqlite3.connect(sql_path)
    cur = con.cursor()
    for item in categorys:
        insert_sql = "insert into category(id,name) values('{0}','{1}')" \
            .format(item.id, item.name)
        cur.execute(insert_sql)
        print(insert_sql)
    con.commit()
    con.close()


def insert_tag(tags):
    con = sqlite3.connect(sql_path)
    cur = con.cursor()
    for item in tags:
        insert_sql = "insert into tag(id,name) " \
                     "select '{0}','{1}' " \
                     "where not exists (select id from tag where id='{0}')" \
            .format(item['id'], item['name'])
        cur.execute(insert_sql)
        print(insert_sql)
    con.commit()
    con.close()


def insert_base_info(images):
    con = sqlite3.connect(sql_path)
    cur = con.cursor()
    for item in images:
        insert_sql = "insert into image(image_id,category_id,image_url,image_url_thumb) values('{0}','{1}','{2}','{3}')" \
            .format(item.image_id, item.category_id, item.image_url, item.image_url_thumb)
        cur.execute(insert_sql)
        print(insert_sql)
    con.commit()
    con.close()


def insert_other_info(image_info):
    con = sqlite3.connect(sql_path)
    cur = con.cursor()
    insert_tag(image_info.tags)
    tag_id = ','.join([item['id'] for item in image_info.tags])
    update_sql = "update image " \
                 "set image_name='{0}',width='{1}',height='{2}',file_type='{3}',file_size='{4}',tags='{5}'" \
                 "where image_id='{6}'".format(image_info.name, image_info.width, image_info.height,
                                               image_info.file_type, image_info.file_size,
                                               tag_id, image_info.image_id)
    print(update_sql)
    cur.execute(update_sql)
    con.commit()
    con.close()


def _test():
    init_sql()

if __name__=='__main__':
    _test()