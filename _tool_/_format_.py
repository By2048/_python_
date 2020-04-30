import json

from veryprettytable import VeryPrettyTable


def format_json(data, empty=True, father_key='', start='||', ignore=None, replace=None):
    ignore = [] if ignore is None else ignore
    replace = [] if replace is None else replace  # [()]

    def run(data, empty, father_key, start, ignore, replace):
        result = []
        for key in list(data):
            value = data[key]

            if not empty:  # 不允许为空的value值
                if not value:
                    continue

            if key in ignore:
                continue

            for item in replace:  # 需要进行key值替换
                key = item[1] if item[0] == key else key

            if isinstance(value, list):
                for _value in value:
                    if isinstance(_value, dict):
                        father_key = key
                    result += run(_value, empty, father_key, '[]', ignore, replace)
            elif isinstance(value, dict):
                result += run(value, empty, key, '{}', ignore, replace)
            else:

                _data = f"{start}"
                _data += f"{f'{father_key}:' if father_key else ''}"
                _data += f"{key}:{value}" if key or value else ""
                result.append(_data)

        return result

    result = run(data, empty, father_key, start, ignore, replace)
    result = ' '.join(result)
    return result


def format_dict_to_table(data: dict, delete=None, show_type=False):
    delete = delete or []
    table = VeryPrettyTable()

    field_names = ["key", "value"]
    if show_type:
        field_names += ["type"]
    table.field_names = field_names

    table.align['key'] = 'r'
    table.align['value'] = 'l'
    if show_type:
        table.align['type'] = 'l'

    for _key, _value in data.items():
        if _key in delete:
            continue
        row = [_key, _value] if not show_type else [_key, _value, f"{type(_value)}"]
        table.add_row(row)

    return f"{table.get_string()}"


def format_frame_hex(data: str):
    nums = '₀₁₂₃₄₅₆₇₈₉⁰¹²³⁴⁵⁶⁷⁸⁹'
    for item in nums:
        data = data.replace(item, ' ')
    data = data.replace('  ', ' ')
    data = data.lstrip().rstrip()
    return data


def format_frame_int(data: str):
    nums = '₀₁₂₃₄₅₆₇₈₉⁰¹²³⁴⁵⁶⁷⁸⁹'
    for item in nums:
        data = data.replace(item, ' ')
    data = data.replace('  ', ' ')
    data = data.lstrip().rstrip()
    data = [int(item, 16) for item in data.split(' ')]
    data = [str(item) for item in data]
    data = ' '.join(data)
    return data


if __name__ == '__main__':
    data = {
        'device_mac': 'CC50E305B972',
        'name': [{"POWER": 1}, {"LIGHT": 0}],
        'functions': {"POWER": 1, "LAMP": 0},
    }
    print(1, format_json(data))
    print(2, format_json(data, empty=False))
    print(3, format_json(data, ignore=['name']))
    print(4, format_json(data, replace=[('name', '_new_name_')]))
    print('\n', "*" * 99, '\n')

    print(format_dict_to_table(data))
    print('\n', "*" * 99, '\n')

    data = 'A5₀02₁00₂FF₃15₄00₅10₆01₇C8₈3C₉E6₁₀3C₁₁00₁₂B4₁₃01₁₄2C₁₅17₁₆34₁₇0B₁₈B8₁₉00₂₀00₂₁3C₂₂'
    print(1, format_frame_hex(data))
    print(2, format_frame_int(data))
    print('\n', "*" * 99, '\n')

    data = {
        'data': [
            {"name": "POWER", "value": 1}, {"name": "Save1", "value": 0}, {"name": "BODY_LOCK", "value": 0},
            {"name": "LAMP", "value": 1}, {"name": "STATE", "value": 1}, {"name": "MODEL", "value": 4100},
            {"name": "SET_TEMPE", "value": 220}, {"name": "Suggest_Temp_Down", "value": 60},
            {"name": "Suggest_Temp_Up", "value": 230}, {"name": "CUR_TEMPE", "value": 213},
            {"name": "SET_WORK_TIME", "value": 3600}, {"name": "Suggest_Time_Down", "value": 300},
            {"name": "Suggest_Time_Up", "value": 5940}, {"name": "REMAIN_WORK_TIME", "value": 3600},
            {"name": "System_Status", "value": 0}, {"name": "ERROR", "value": 0}
        ]
    }
    print(1, format_json(data, empty=False))
