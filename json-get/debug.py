import json


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


def insert_item(dict_in, key_in, value_in):
    for k, v in dict_in.items():
        if k==key_in:
            dict_in[k].append({value_in:[]})
            return dict_in
        else:
            for item in dict_in[k]:
                insert_item(item,key_in,value_in)



def print_all(dict_in):
    for k, v in dict_in.items():
        print(k)
        if isinstance(v, list) and len(v) == 0:
            return dict_in
        else:
            for item in dict_in[k]:
                print_all(item)


first_line = {"奴隶社会": [{"非洲": []}, {"亚洲": []}, {"欧洲": []}]}

# {"古印度": []}


print(first_line)

print(first_line["奴隶社会"])
# first_line["奴隶社会"].append({"古印度": []})
print(first_line["奴隶社会"][1]["亚洲"])
# first_line["奴隶社会"][1]["亚洲"].append({"古印度": []})
print(first_line)


print('-'*99)
insert_item(first_line, "亚洲", "古印度")
print(first_line)

insert_item(first_line, "古印度", "test-item")
print(first_line)


'''
{
    "奴隶社会": [{
        "非洲": []
    }, {
        "亚洲": [{
            "古印度": []
        }]
    }, {
        "欧洲": []
    }]
}
'''


if 2 in is_in(first_line,"亚洲","古印度"):
    print('T')
else:
    print('F')


