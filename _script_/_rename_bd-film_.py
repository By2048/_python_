try:
    from ._rename_ import Rename
except ImportError:
    from _rename_ import Rename


def need_rename(item):
    result = 'bd-film.cc' in item
    return result


def get_name(item):
    name = item.lstrip('[BD影视分享bd-film.cc]')
    name = name.strip()
    name = name.replace(':', ' ')
    name = name.replace('：', ' ')
    _name_, *_, _type_ = name.split('.')
    return f"{_name_}.{_type_}"


if __name__ == '__main__':
    rename = Rename()
    rename.folder = "T:\\"
    rename.function_need_rename = need_rename
    rename.function_get_name = get_name
    rename.show_title = False
    rename.init()
    print(rename)
    rename.start()
