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
for line in all_line:
    print(line)

new_line=[['' for i in range(4)] for j in range(10)]


all_list_line = [line.split(',') for line in all_line]

for line in all_list_line:
    print(line)
print('--------------------')
for i in range(4):
    new_line[0][i]=all_list_line[0][i]

def get_len(line):
    cnt=0
    for item in line:
        if item !='':
            cnt+=1
    return cnt

for i in range(10):
    for j in range(4):
        if all_list_line[i][j]=='':
            new_line[i][j]=new_line[i-1][j]
        else:
            new_line[i][j]=all_list_line[i][j]





def insert_end(dict_in, item):
    for k, v in dict_in.items():
        if isinstance(v, list) and len(v) == 0:
            dict_in[k] = [{item: []}]
            return dict_in
        else:
            insert_end(dict_in[k][0], item)


def is_in(dict_in,key_in,value_in,cnt=0,tmps=[]):
    tmps.append(cnt)
    print(tmps)
    for k,v in dict_in.items():
        if k==key_in:
            cnt+=1
            if dict_in[k]==[{value_in:[]}]:
                cnt+=1
            for _item in dict_in[k]:
                is_in(_item,value_in,value_in,cnt,tmps)
        else:
            for item in dict_in[k]:
                is_in(item,key_in,value_in,cnt,tmps)

    return tmps

def in_no(dict,key,value):
    tmps=[]
    if 2 in is_in(dict, key,value,tmps=tmps):
        return True
    else:
        return False

def insert_item(dict_in, key_in, value_in):
    for k, v in dict_in.items():
        if is_in == True:
            break
        if k==key_in:
            if in_no(dict_in,key_in,value_in)==False:
                dict_in[k].append({value_in:[]})
        else:
            for item in dict_in[k]:
                insert_item(item,key_in,value_in)

for line in new_line:
    print(line)
print('='*88)


test_dict={'奴隶社会':[]}
for item in new_line[0][1:]:
    insert_end(test_dict,item)
# print(test_dict)
for line in new_line[1:]:
    cnt=len(line)-1
    for (i,item) in zip(range(cnt),line[1:]):
        insert_item(test_dict,line[i],item)

print(json.dumps(test_dict,ensure_ascii=False))
print(json.dumps(test_dict,ensure_ascii=False,indent=4))


# for item in


