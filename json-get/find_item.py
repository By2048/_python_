import json

json_info = {"奴隶社会": [{"非洲": [{"古埃及文明": [{"金字塔": []}]}]},
                      {"亚洲": [{"两河流域文明": [{"汉谟拉比法典": []}]}, {"古印度": [{"种姓制度": []}, {"佛教的创立": []}]}]}, {
                          "欧洲": [{"希腊": [{"希腊城邦": []}, {"雅典民主": []}]}, {"罗马": [{"城邦": []}, {"帝国的征服与扩展": []}]},
                                 {"希腊罗马古典文化": [{"建筑艺术": []}, {"公历": []}]}]}]}

print(json_info)

all_leave = []
all_key = []


def get_all_key(dict_in, leave=0):
    for k, v in dict_in.items():
        leave += 1
        all_leave.append(leave)
        all_key.append(k)
        print(leave, end='  ')
        print(k)
        if dict_in[k] != []:
            for _item in dict_in[k]:
                get_all_key(_item, leave)
        else:
            for item in dict_in[k]:
                get_all_key(item, leave)


dict_test = eval(str(json_info))

get_all_key(dict_test)

print(all_leave)
print(all_key)


def find_item(item_key):
    _index=0
    _leave=0
    all_path = []
    if item_key not in all_key:
        return '不存在关键字:' + item_key
    for (index,leave, key) in zip(range(len(all_leave)),all_leave, all_key):
        if item_key == key:
            all_path.append(key)
            _leave=leave
            _index=index
    else:
        for (leave, key) in zip(all_leave[_index-1::-1], all_key[_index-1::-1]):
            if leave==_leave-1:
                all_path.append(key)
                _leave-=1
    return all_path[::-1]


path=find_item('希腊城邦')
print(path)





# test_list=['帝国的征服与扩展', '希腊罗马古典文化', '欧洲', '奴隶社会']
# print(test_list)
# print(test_list[2::-1])