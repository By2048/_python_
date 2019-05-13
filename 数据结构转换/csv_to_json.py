import csv
import json
from pprint import pprint


def get_data(path):
    data = []

    with open(path, encoding='utf-8-sig') as file:
        data = [item.rstrip('\n') for item in file]

    data = [item.split(',') for item in data]

    breakpoint()

    for index_i, value_i in enumerate(data):
        for index_j, value_j in enumerate(value_i):
            if not value_j:
                data[index_i][index_j] = data[index_i - 1][index_j]

    return data


def get_len(line):
    cnt = 0
    for item in line:
        if item != '':
            cnt += 1
    return cnt


def init_data(data, item):
    for k, v in data.items():
        print(k, v)
        if isinstance(v, list) and len(v) == 0:
            data[k] = [{item: []}]
            return data
        else:
            init_data(data[k][0], item)


def is_in(dict_in, key_in, value_in, cnt=0, tmps=[]):
    tmps.append(cnt)
    for k, v in dict_in.items():
        if k == key_in:
            cnt += 1
            if dict_in[k] == [{value_in: []}]:
                cnt += 1
            for _item in dict_in[k]:
                is_in(_item, value_in, value_in, cnt, tmps)
        else:
            for item in dict_in[k]:
                is_in(item, key_in, value_in, cnt, tmps)
    return tmps


def in_no(dict, key, value):
    tmps = []
    if 2 in is_in(dict, key, value, tmps=tmps):
        return True
    else:
        return False


def insert_item(dict_in, key_in, value_in):
    for k, v in dict_in.items():
        if is_in == True:
            break
        if k == key_in:
            if in_no(dict_in, key_in, value_in) == False:
                dict_in[k].append({value_in: []})
        else:
            for item in dict_in[k]:
                insert_item(item, key_in, value_in)


def csv2json(file_path):
    data = get_data(path)

    first_key = data[0][0]

    json_dict = {first_key: []}

    for item in data[0][1:]:
        init_data(json_dict, item)

    # print(json_dict)

    for line in data[1:]:
        cnt = len(line) - 1
        for (i, item) in zip(range(cnt), line[1:]):
            insert_item(json_dict, line[i], item)
    json_data = json.dumps(json_dict, ensure_ascii=False, indent=4)
    return json_data


if __name__ == '__main__':
    path = r'data.csv'
    data = get_data(path)
    pprint(data)
    # data = get_new_line(data)
    # json_data = csv2json(path)
    # print(json_data)
