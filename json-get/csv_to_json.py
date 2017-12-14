import json


def get_line(file_path):
    lines = []
    with open(file_path, encoding='utf-8-sig') as file:
        for row in file:
            row = row.replace('\n', '')
            lines.append(row)
    return lines


def get_new_line(all_line):
    list_line = [line.split(',') for line in all_line]

    len_i = len(list_line)
    len_j = len(list_line[0])

    new_line = [['' for j in range(len_j)] for j in range(len_i)]

    # 先获取第一行
    for j in range(len_j):
        new_line[0][j] = list_line[0][j]

    # 转换其他行
    for i in range(len_i):
        for j in range(len_j):
            if list_line[i][j] == '':
                new_line[i][j] = new_line[i - 1][j]
            else:
                new_line[i][j] = list_line[i][j]

    return new_line


def get_len(line):
    cnt = 0
    for item in line:
        if item != '':
            cnt += 1
    return cnt


def insert_end(dict_in, item):
    for k, v in dict_in.items():
        if isinstance(v, list) and len(v) == 0:
            dict_in[k] = [{item: []}]
            return dict_in
        else:
            insert_end(dict_in[k][0], item)


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
    all_line = get_line(path)
    new_line = get_new_line(all_line)

    first_key = new_line[0][0]

    json_dict = {first_key: []}
    for item in new_line[0][1:]:
        insert_end(json_dict, item)

    for line in new_line[1:]:
        cnt = len(line) - 1
        for (i, item) in zip(range(cnt), line[1:]):
            insert_item(json_dict, line[i], item)
    json_data = json.dumps(json_dict, ensure_ascii=False, indent=4)
    return json_data


if __name__ == '__main__':
    path = r'E:\Desktop\思维导图.csv'
    json_data = csv2json(path)
    print(json_data)
