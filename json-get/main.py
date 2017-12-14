import csv
import json

all_line = []
data = {}
file_path = r'E:\Desktop\csv.csv'


def get_line():
    with open(file_path, encoding='utf-8-sig') as file:
        # first_file=file[0]
        # print(first_file)
        for row in file:
            row = row.replace('\n', '')
            all_line.append(row)


get_line()
# print('\n'.join(all_line))
# print('------------------')

first_line = all_line[0]
first_list_line = first_line.split(',')
first_item = first_list_line[0]
print(first_item)

all_list_line = [line.split(',') for line in all_line]
all_list_line[0][0] = ''

for line in all_list_line:
    print(line)


def get_empty_num(list_line):
    print(list_line.count(''))


# for list_line in all_list_line[1:]:
#     get_empty_num(list_line)
#     for item in list:
#         data[first_item] = list_line[1:]

test_line=['非洲', '古埃及文明', '金字塔']
test_dir={'社会':[]}
def insert_dir(root_dir, insert_dir):
    for item in test_line:
        pass
print(test_dir)


# insert_dir(first_item, )
# print(json.dumps(all_list_line))

print('----------------')

test_data={"奴隶社会": [{"非洲": []}, {"亚洲": []}, {"欧洲": []}]}
print(test_data)
# print(test_data['奴隶社会'][0])

# test_data['非洲'].append({'---':[]})
# print(test_data['非洲'])

# print(json.dumps(test_data),)


print('----------------------------')
from collections import defaultdict
def make_dict():
    return defaultdict(make_dict)

class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value



# a = AutoVivification()
# # a['奴隶社会']
# a['奴隶社会']['非洲']=[]
# a['奴隶社会']['非洲']
# a['奴隶社会']['亚洲']=[]
# a['奴隶社会']['欧洲']=[]
#
# # a['1']['2']['3'] = '4'
# # a['1']['3']['3'] = '5'
# # a['1']['2']['test'] = '6'
#
# print (a)
#











