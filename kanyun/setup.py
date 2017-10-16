import os
try:
    from .get_summary_md import *
except ImportError:
    from get_summary_md import *

try:
    from .get_empty_folder_md import *
except ImportError:
    from get_empty_folder_md import *

try:
    from .get_push_bat import *
except ImportError:
    from get_push_bat import *


start_path='E:\\Desktop\\NoteBook'

def get_all_note_path():
    print('\n')
    note_paths=[]
    paths = os.listdir(start_path)
    for path in paths:
        if path not in ['.git','.gitignore','README.md','.cmd']:
            note_path=os.path.join(start_path,path)
            note_paths.append(note_path)
            print(note_path)
    print('\n')
    return note_paths




if __name__=='__main__':
    paths=get_all_note_path()
    for path in paths:
        create_md(path)
        create_summary(path)
    # create_push_bat()
