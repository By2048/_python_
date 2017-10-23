try:
    from get_summary_md import *
    from get_empty_folder_md import *
    from get_push_bat import *
except ImportError:
    from .get_summary_md import *
    from .get_empty_folder_md import *
    from .get_push_bat import *

start_path='E:\\Desktop\\NoteBook'

def get_all_note_path():
    note_paths=[]
    paths = os.listdir(start_path)
    for path in paths:
        if path[0]=='.' or path=='README.md':
            continue
        note_path=os.path.join(start_path,path)
        note_paths.append(note_path)

    return note_paths


if __name__=='__main__':
    print('\n')
    paths=get_all_note_path()
    print('\n'.join(paths))
    print('\n')
    for path in paths:
        create_md(path)
        create_summary(path)

    # create_push_bat()
