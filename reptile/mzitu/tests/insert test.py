import os,datetime
import pyodbc

con_text = pyodbc.connect('DRIVER={SQL Server};SERVER=.;DATABASE=ImageSite;UID=Link-ImageSite;PWD=P@ssw0rd')


rootDir = "F:\\Image\\mzitu"
# os.path.getmtime(name)
# print(os.listdir(rootDir))

# print(len(files))

# def get_folder_info(root):
#     create_date = datetime.datetime.fromtimestamp(os.path.getctime(root)).strftime('%Y-%m-%d %H:%M:%S')
# print(root.split('\\')[-1])

#     name = os.path.splitext(root)[0].split('\\')[-2]
#     img_num=
#     total_size=

class Folder:
    Name = ""
    Path = ""
    CreateDate = ""  # 文件夹创建时间
    ImgNum = ""
    TotalSize = ""
    def __init__(self, name, path, createDate, imgNum, totalSize):
        self.Name = name
        self.Path = path
        self.CreateDate = createDate
        self.ImgNum = imgNum
        self.TotalSize = totalSize

def get_folder_info(root,files):
    try:
        create_date = datetime.datetime.fromtimestamp(os.path.getctime(root)).strftime('%Y-%m-%d %H:%M:%S')
        name = root.split('\\')[-1]
        path=root
        img_num=str(len(files))
        _size=sum([os.path.getsize(os.path.join(root, name)) for name in files])/1024/1024
        total_size=str(round(_size,2))
    except:
        pass
    if img_num==0:
        return Folder('','','','','')
    else:
        return Folder(name,path,create_date,img_num,total_size)

def get_folder_id(folder_name):
    print(folder_name)
    try:
        sql_cursor = con_text.cursor()
        sql="select Id from Folders where Name='{0}'".format(folder_name)
        sql_cursor.execute(sql)
        print(sql+'------')
        row = sql_cursor.fetchone()
    except:
        return '0'
    return str(row.Id)

def insert_folders(folder):
    if folder.ImgNum=='0':
        pass
    else:
        insert = "insert into [Folders] ([Name],[Path],[CreateDate],[ImgNum],[TotalSize])"
        values = "values ('{0}', '{1}', '{2}', '{3}', '{4}')" \
            .format(folder.Name, folder.Path, folder.CreateDate,folder.ImgNum,folder.TotalSize)
        insert_sql = insert + '\n' + values
        # sql_cursor = con_text.cursor()
        # sql_cursor.execute(insert_sql)
        # con_text.commit()

def folder_print(folder):
    print(folder.Name)
    print(folder.Path)
    print(folder.CreateDate)
    print(folder.ImgNum)
    print(folder.TotalSize)
    print('\n')

# if __name__ == "__main__":
#     rootDir = "F:\\Image\\mzitu"
#     for root, dirs, files in os.walk(rootDir):
#         print(root)
#         folder=get_folder_info(root,files)
#         folder_print(folder)
#         insert_folders(folder)
#         pp=get_folder_id(folder.Name)
#         print(pp)


def clean_image_site():
    sql_cursor = con_text.cursor()
    sql_cursor.execute("delete from Images ")
    con_text.commit()
    sql_cursor.execute("delete from Folders")
    con_text.commit()

clean_image_site()