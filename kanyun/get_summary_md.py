import os
import functools

class MDLine:
    Level=0
    Folder=''
    SplitPaths=[]
    def __init__(self,level,folder,splitPaths):
        self.Level=level
        self.Folder=folder
        self.SplitPaths=splitPaths

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

md_lines=[]
lines=[]

def get_summary(rootDir, level=1):
    # if level == 1:
    #     print(rootDir)
    for folder in os.listdir(rootDir):
        if folder.endswith('.json') or folder[0] in ['_','.'] or folder=='SUMMARY.md':
            continue
        path = os.path.join(rootDir, folder)
        if os.path.isdir(path)==True:
            split_path =(path+'\\'+folder+'.md').split('\\')[-level-1:]
        else:
            split_path = (rootDir + '\\' + folder).split('\\')[-level:]

        # print(split_path)

        md_line=MDLine(level,folder,split_path)
        md_lines.append(md_line)

        # line=''
        # line+=' '* (level - 1)*4+'* '+'['+folder+']'+'('+my_join(split_path)+')'
        # line=line.replace('\\','/')
        # lines.append(line)

        if is_equal(split_path)==True:
            if os.path.isfile(path)==True:
                # lines.pop()
                md_lines.pop()

        if os.path.isdir(path):
            get_summary(path, level + 1)

    return lines

def my_cmp_md(item1,item2):
    cnt1=len(item1.SplitPaths)
    cnt2=len(item2.SplitPaths)
    if cnt2==1:
        return -1
    else:
        return 0


def get_lines_by_md_line():
    md_lines.sort(key=functools.cmp_to_key(mycmp=my_cmp_md))
    for md_line in md_lines:
        # print(md_line.SplitPaths)
        line=''
        line+=' '* (md_line.Level - 1)*4+'* '+'['+md_line.Folder+']'+'('+my_join(md_line.SplitPaths)+')'
        line=line.replace('\\','/')
        lines.append(line)


def keep_summary(start_path):
    summary_path = start_path + '\\' + 'SUMMARY.md'
    print('create summary.md    '+summary_path)
    with open(summary_path, 'w+', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            file.write('\n')
    file.close()
    clean()

def clean():
    md_lines.clear()
    lines.clear()



def create_summary(path):
    get_summary(path)
    get_lines_by_md_line()
    keep_summary(path)

if __name__=='__main__':
    # Test...
    start_path = r'F:\- Test\android'
    get_summary(start_path)
    get_lines_by_md_line()
    keep_summary(start_path)
    pass


