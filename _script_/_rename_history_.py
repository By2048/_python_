from datetime import datetime

try:
    from ._rename_ import Rename
except ImportError:
    from _rename_ import Rename


def need_rename(item):
    result = "Screenshot_" in item
    return result


def get_name(item):
    _old_ = item
    _name_, _type_ = item.split("Screenshot_")[-1].split('.')
    _name_ = datetime.strptime(_name_, "%Y%m%d%H%M%S").strftime("%Y-%m-%d %H-%M-%S")
    _new_ = f"{_name_}.{_type_}"
    return _new_


def main():
    rename = Rename()
    rename.folder = "R:\\History\\"
    rename.function_need_rename = need_rename
    rename.function_get_name = get_name
    rename.init()
    print(rename)
    rename.start()


if __name__ == "__main__":
    main()
