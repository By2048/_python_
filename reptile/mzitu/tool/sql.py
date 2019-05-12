# coding=utf-8
import logging

try:
    from mzitu.conf.sql import db_reptile as db
    from mzitu.tool.model import Meizi
except ImportError:
    from conf.sql import db_reptile as db
    from tool.model import Meizi


# def insert_download(meizi: Meizi):
#
#
#
#     try:
#         insert = "insert into download (id,link,name,category,date,downloads) "
#         fmt = "values ('{0}','{1}','{2}','{3}','{4}','{5}')"
#         param = [meizi.id, meizi.link, meizi.name, meizi.category, meizi.date, ','.join(meizi.downloads)]
#         sqlite_cursor.execute(insert + fmt.format(*param))
#         sqlite_connect.commit()
#     except Exception as e:
#         logging.error('插入数据库失败 ' + str(e))
#
#     try:
#         with open(download_txt_path, 'a', encoding='utf-8') as file:
#             file.write(str(meizi).strip() + '\n')
#     except Exception as e:
#         logging.error('写入文件失败 ' + str(e))


# def insert_error(meizi: Meizi):
#     try:
#         insert = "insert into error (link,name) "
#         fmt = "values ('{0}','{1}')"
#         param = [meizi.link, meizi.name]
#         sqlite_cursor.execute(insert + fmt.format(*param))
#         sqlite_connect.commit()
#     except Exception as e:
#         logging.error('插入数据库失败 ' + str(e))
#

# def get_downloads():
#     sqlite_cursor.execute("select link from download")
#     downloads = []
#     for item in sqlite_cursor.fetchall():
#         downloads.append(item[0])
#     return downloads


def insert_download(meize: Meizi, status=True):
    try:
        data = meize.serialization()
        data['status'] = status
        db.mzitu.insert(data)
    except Exception as e:
        logging.exception(e)


def get_downloads():
    downloads = []
    try:
        for item in db.mzitu.find({}):
            downloads.append(item['id'])
    except Exception as e:
        logging.exception(e)
    return downloads


# def get_errors():
#     sqlite_cursor.execute("select link from error")
#     errors = []
#     for item in sqlite_cursor.fetchall():
#         errors.append(item[0])
#     return errors


if __name__ == '__main__':
    pass
