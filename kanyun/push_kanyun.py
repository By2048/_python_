import io
import os

start_path='E:\\Desktop\\NoteBook'

note_paths = []
git_paths = []

def get_all_note_path():
    paths = os.listdir(start_path)
    for path in paths:
        if path not in ['.git','.gitignore','README.md']:
            git_path='https://git.kancloud.cn/am-note/'+path.lower()+'.git'
            git_paths.append(git_path)
            note_path = os.path.join(start_path, path)
            note_paths.append(note_path)

def run_cmd(cmd):
    lines=[]
    for line in os.popen(cmd).readlines():
        lines.append(line.replace('''\n''',''))
    return lines


get_all_note_path()
print(note_paths)
print(git_paths)


print(os.popen('dir').readlines())

# for line in os.popen('dir').readlines():
#     line=line.replace('''\n''','')
#     print(line)
#
tmps=run_cmd('cd /d E:\\Desktop\\NoteBook\\Android \n dir')
for tmp in tmps:
    print(tmp)

# tmps=run_cmd('dir')
# for tmp in tmps:
#     print(tmp)