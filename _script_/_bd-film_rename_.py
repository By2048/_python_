import os

path = 'T:\\'
videos = []

try:
    from ._rename_ import File, init_files_info, print_files_info, rename_files
except ImportError:
    from _rename_ import File, init_files_info, print_files_info, rename_files


def init():
    for item in os.listdir(path):
        if 'bd-film.cc' not in item:
            continue
        old = item
        file = File(folder=path, old_name=old)
        videos.append(file)


def get_name(name):
    name = name.lstrip('[BD影视分享bd-film.cc]')
    name = name.strip()
    name = name.replace(':', ' ')
    name = name.replace('：', ' ')
    _name_, *_, _type_ = name.split('.')
    return f"{_name_}.{_type_}"


if __name__ == '__main__':
    init()
    init_files_info(videos, get_name)
    print_files_info(videos)
    rename_files(videos)
