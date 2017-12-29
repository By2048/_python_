import os


all_categery=[]

def Tree(rootDir, level=1):
    if level == 1:
        pass
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        if path.endswith('.md'):
            all_categery.append('<li>'+lists+'</li>')
        if os.path.isdir(path):
            all_categery.append('<h3>')
            all_categery.append(path)
            all_categery.append('</h3>')
            Tree(path, level + 1)


def get_item(path):
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path,item)):
            all_categery.append('<ul>{}</ul>'.format(item))
        else:
            all_categery.append('<li>{}</li>'.format(item))


get_item(r'f:\notebook\python')


for item in all_categery:
    print(item)

a=[1,2,3,4]
print(a)
print(a[:-1])








# 文件夹遍历 Dos Tree 效果
# def Tree(rootDir, level=1):
#     # 实现类 Dos Tree 效果
#     if level == 1:
#         print(rootDir)
#     for lists in os.listdir(rootDir):
#         path = os.path.join(rootDir, lists)
#         print('│  ' * (level - 1) + '│--' + lists)
#         if os.path.isdir(path):
#             Tree(path, level + 1)



# # 保存文件信息 TXT 格式
# def keep_insert(sql):
#     try:
#         sql = sql.encode('gbk', 'ignore').decode('gbk', 'ignore')
#         file = open("insert_sql.txt", "a")
#         file.writelines("go" + "\n" + sql + "\n\n")
#     except:
#         file.writelines("-- False" + "\n")
#     finally:
#         file.close()


