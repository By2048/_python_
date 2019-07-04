import os
import json
import functools

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


rootDir='f:\\- test\\c-sharp'
Tree(rootDir, level=1)




def get_all_md_path(rootPath):
    all_path=[]
    for root, dirs, files in os.walk(rootPath):
        for file in files:
            if file.endswith('.md'):
                file_path=os.path.join(root, file)
                file_path=file_path.replace(start_path,'')
                all_path.append(file_path[1:])
    return all_path




json_data={}
json_str=json.dumps(json_data)
json_data=json.loads(json_str)

def get_summary_by_md_path(paths):
    for path in paths:
        list=path.split('\\')
        json_data[list[0]]=list[1:]
        # for json_item in path.split('\\')[0]:
        #     if(json_data[json_item])

    return




# for path in paths:
#     lists = path.split('\\')
#     if len(lists) >= 2:
#         print(lists[0],end="   ")
#         print(lists[1:])

# if json_data[lists[0]]=="":
#     json_data[lists[0]] = lists[1:]
# else:
#     json_data[lists[0]]+=lists[1:]

# json_str = json.dumps(json_data)
# print(json_str)

# for path in paths:
#     lists=path.split('\\')
#     # print(lists)
#     all_list.append(lists)

# for list in lists:
#
# if json_data[list[0]]==None:
#     json_data[list[0]] = list[1]
# else:
#     json_data[list[0]]+=
# if len(list)>=2:
#     print(list[1:])
# json_data[list[0]]=list[1:]
# print(json_data[list[0]])

# print(p)

# 文件夹遍历 Dos Tree 效果