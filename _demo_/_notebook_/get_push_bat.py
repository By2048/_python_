import io
import os

try:
    from config import *
    from tool import *
except ImportError:
    from .config import *
    from .tool import *


def run_cmd(cmd):
    lines = []
    for line in os.popen(cmd).readlines():
        lines.append(line.replace('''\n''', ''))
    for line in lines:
        print(line)


# 创建推送到看云的脚本  备用
def create_cmd_file(folder_name):
    file_path = cmd_keep_path + '\\' + folder_name + '.bat'
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('E:' + '\n')
        file.write('cd /d E:\\Desktop\\NoteBook\\' + folder_name + '\n')
        file.write('git init' + '\n')
        file.write('git add *' + '\n')
        file.write('git remote add origin https://git.kancloud.cn/am-note/' + folder_name.lower() + '.git' + '\n')
        file.write('git commit -m "commit"' + '\n')
        file.write('git push -f origin master' + '\n')
        file.write('pause' + '\n')
    file.close()


def create_push_bat():
    print('\n\ncreate .cmd')
    for note_path in get_all_note_path():
        folder_name = os.path.basename(note_path)
        create_cmd_file(folder_name)


if __name__ == '__main__':
    # Test...
    pass
