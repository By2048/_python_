import os

def my_join(lists):
    path=''
    for list in lists[:-1]:
        path+=list+'\\'
    path+=lists[len(lists)-1]
    return path

def is_exit_md(list):
    item =list[len(list)-1]
    print(str(item[-2:]))
    if str(item[-2:])=='md':
        return True
    else:
        return False

def is_equal(list):
    if len(list)==1:
        return False
    item1=list[-1]
    item2=list[-2]
    if item1[:-3]==item2:
        return True
    else:
        return False

lines=[]
def get_summary(rootDir, level=1):
    # if level == 1:
    #     print(rootDir)
    for list in os.listdir(rootDir):
        if list.endswith('.json') or list in ['images','SUMMARY.md','.git']:
            continue
        path = os.path.join(rootDir, list)
        if os.path.isdir(path)==True:
            split_path =(path+'\\'+list+'.md').split('\\')[-level-1:]
        else:
            split_path = (rootDir + '\\' + list).split('\\')[-level:]

        line=''
        line+=' '* (level - 1)*4+'* '+'['+list+']'+'('+my_join(split_path)+')'
        line=line.replace('\\','/')
        lines.append(line)

        if is_equal(split_path)==True:
            if os.path.isfile(path)==True:
                lines.pop()

        if os.path.isdir(path):
            get_summary(path, level + 1)

    return lines

def keep_summary(start_path):
    summary_path = start_path + '\\' + 'SUMMARY.md'
    with open(summary_path, 'w+', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            file.write('\n')
    file.close()
    clean()

def clean():
    lines.clear()




if __name__=='__main__':
    start_path = r'F:\- Test\c-sharp'
    get_summary(start_path)
    keep_summary(start_path)
    pass


