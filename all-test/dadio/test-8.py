# 感叹号系列#5：删除单词末尾的所有感叹号


def remove(s):
    all_item=s.split(' ')
    change_item=[]
    for item in all_item:
        if item=='!'*len(item):
            change_item.append(item)
            continue
        else:
            change_item.append(item.rstrip('!'))
    return (' '.join(change_item))




remove('!Hi! !! !Hi!')