import io
import os

start_path='E:\\Desktop\\NoteBook'

folders=[]
note_paths = []
git_paths = []

def get_all_note_path():
    paths = os.listdir(start_path)
    for path in paths:
        if path not in ['.git','.gitignore','README.md','.cmd']:
            git_path='https://git.kancloud.cn/am-note/'+path.lower()+'.git'
            git_paths.append(git_path)
            note_path = os.path.join(start_path, path)
            note_paths.append(note_path)
            folders.append(path)

def run_cmd(cmd):
    lines=[]
    for line in os.popen(cmd).readlines():
        lines.append(line.replace('''\n''',''))
    for line in lines:
        print(line)
    # return lines

get_all_note_path()
# print(note_paths)
# print(git_paths)

# for line in os.popen('dir').readlines():
#     line=line.replace('''\n''','')
#     print(line)


start_cmd_path='E:\\Desktop\\NoteBook\\.cmd'
def create_cmd_file(note_name):
    file_path=start_cmd_path+'\\'+note_name+'.bat'
    with open(file_path,'w',encoding='utf-8') as file:
        file.write('E:'+'\n')
        file.write('cd /d E:\\Desktop\\NoteBook\\'+note_name + '\n')
        file.write('git init' + '\n')
        file.write('git add *' + '\n')
        file.write('git remote add origin https://git.kancloud.cn/am-note/'+note_name.lower()+'.git' + '\n')
        file.write('git commit -m "commit"' + '\n')
        file.write('git push -f origin master' + '\n')
        file.write('pause' + '\n')
    file.close()



# tmps=run_cmd('cd /d E:\\Desktop\\NoteBook\\Android \n dir')
# for tmp in tmps:
#     print(tmp)

# tmps=run_cmd('dir')
# for tmp in tmps:
#     print(tmp)

def create_push_bat():
    print('\n\ncreate .cmd')
    for folder in folders:
        create_cmd_file(folder)

if __name__=='__main__':
    # Test...
    create_push_bat()
