import os
try:
    from .get_summary import *
except ImportError:
    from get_summary import *

try:
    from .add_md import *
except ImportError:
    from add_md import *


start_path='E:\\Desktop\\NoteBook'

def get_all_note_path():
    note_paths=[]
    paths = os.listdir(start_path)
    for path in paths:
        if path not in ['.git','.gitignore','README.md']:
            note_path=os.path.join(start_path,path)
            note_paths.append(note_path)
            print(note_path)
    return note_paths


for path in get_all_note_path():
    create_md(path)
    get_summary(path)
    keep_summary(path)

