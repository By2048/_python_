import os

# 文件夹遍历 Dos Tree 效果
def Tree(rootDir, level=1):
    # 实现类 Dos Tree 效果
    if level == 1:
        print(rootDir)
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        print('│  ' * (level - 1) + '│--' + lists)
        if os.path.isdir(path):
            Tree(path, level + 1)


Tree("f:\\- test\\program",1)

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


