import sqlite3
import os

sql_path = 'T:\\_tmp\\image.db'


# sql_path = '/home/python/wallpaper/image.db'

# ['id', 'width', 'height', 'file_type', 'file_size', 'url_image', 'url_thumb', 'url_page'])

def init_sql():
    if os.path.isfile(sql_path):
        os.remove(sql_path)

    create_category = """create table category
    (
        id     text,
        name   text
    );"""

    create_image = """create table image
    (
        id              text,
        width           text,
        height          text,
        file_type       text,
        file_size       text,
        url_image       text,
        url_thumb       text,
        url_page        text,
        name            text,
        category        text,
        category_id     text,
        sub_category    text,
        sub_category_id text,
        user_name       text,
        user_id         text,      
        tags            text      
    );"""

    create_tag = """create table tag
    (
        id      text,
        name    text
    );"""

    con = sqlite3.connect(sql_path)
    cur = con.cursor()
    cur.execute(create_category)
    cur.execute(create_image)
    cur.execute(create_tag)
    con.commit()
    con.close()


def insert_category(categorys):
    con = sqlite3.connect(sql_path)
    cur = con.cursor()
    for item in categorys:
        insert_sql = "insert into category(id,name) values('{id}','{name}')" \
            .format(id=item.id, name=item.name)
        cur.execute(insert_sql)
        print(insert_sql)
    con.commit()
    con.close()


def insert_tag(tags):
    print(tags)
    con = sqlite3.connect(sql_path)
    cur = con.cursor()
    for tag in tags:
        insert_sql = "insert into tag(id,name) " \
                     "select '{id}','{name}' " \
                     "where not exists (select id from tag where id='{id}')" \
            .format(id=tag['id'], name=tag['name'])
        cur.execute(insert_sql)
        print(insert_sql)
    con.commit()
    con.close()


def insert_base_info(images):
    con = sqlite3.connect(sql_path)
    cur = con.cursor()
    for img in images:
        insert_sql = "insert into image(id,width,height,file_type,file_size,url_image, url_thumb, url_page) " \
                     "values('{id}','{width}','{height}','{file_type}','{file_size}','{url_image}','{url_thumb}','{url_page}')" \
            .format(id=img.id, width=img.width, height=img.height, file_type=img.file_type, file_size=img.file_size,
                    url_image=img.url_image, url_thumb=img.url_thumb, url_page=img.url_page)
        print(insert_sql)
        cur.execute(insert_sql)
    con.commit()
    con.close()


def insert_other_info(image):
    con = sqlite3.connect(sql_path)
    cur = con.cursor()
    insert_tag(image.tags)
    update_sql = "update image " \
                 "set name='{0}',category='{1}',category_id='{2}',sub_category='{3}',sub_category_id='{4}',user_name='{5}',user_id='{6}',tags=\"{7}\"" \
                 " where id='{8}'" \
        .format(image.name, image.category, image.category_id, image.sub_category, image.sub_category_id,
                image.user_name, image.user_id, image.tags, image.id)
    print(update_sql)
    cur.execute(update_sql)
    con.commit()
    con.close()


def get_image_id():
    con = sqlite3.connect(sql_path)
    cur = con.cursor()
    cur.execute("SELECT * FROM image WHERE category IS NULL")
    all_image_id = [item[0] for item in cur.fetchall()]
    return all_image_id



if __name__ == '__main__':
    init_sql()