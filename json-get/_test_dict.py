from collections import defaultdict
import json

# tmp_dir_0={'a':[]}
# tmp_dir_1={'b':[]}
# tmp_dir_2={'c':[]}
# tmp_dir_3={'d':[]}
#
# print(tmp_dir_0)
#
# tmp_dir_0['a'].append(tmp_dir_1)
# print(tmp_dir_0)
#
#
# print(tmp_dir_0['a'])

'''
奴隶社会,非洲,古埃及文明,金字塔
,亚洲,两河流域文明,汉谟拉比法典
,,古印度,种姓制度
,,,佛教的创立
,欧洲,希腊,希腊城邦
,,,雅典民主
,,罗马,城邦
,,,帝国的征服与扩展
,,希腊罗马古典文化,建筑艺术
,,,公历

['奴隶社会', '非洲', '古埃及文明', '金字塔']
['', '亚洲', '两河流域文明', '汉谟拉比法典']
['', '', '古印度', '种姓制度']
['', '', '', '佛教的创立']
['', '欧洲', '希腊', '希腊城邦']
['', '', '', '雅典民主']
['', '', '罗马', '城邦']
['', '', '', '帝国的征服与扩展']
['', '', '希腊罗马古典文化', '建筑艺术']
['', '', '', '公历']

['奴隶社会', '非洲', '古埃及文明', '金字塔']
['奴隶社会', '亚洲', '两河流域文明', '汉谟拉比法典']
['奴隶社会', '亚洲', '古印度', '种姓制度']
['奴隶社会', '亚洲', '古印度', '佛教的创立']
['奴隶社会', '欧洲', '希腊', '希腊城邦']
['奴隶社会', '欧洲', '希腊', '雅典民主']
['奴隶社会', '欧洲', '罗马', '城邦']
['奴隶社会', '欧洲', '罗马', '帝国的征服与扩展']
['奴隶社会', '欧洲', '希腊罗马古典文化', '建筑艺术']
['奴隶社会', '欧洲', '希腊罗马古典文化', '公历']

隶社会,非洲
,亚洲
,,古印度
,欧洲

奴隶社会
奴隶社会,非洲
奴隶社会,亚洲
奴隶社会,亚洲,古印度
奴隶社会,欧洲
'''


tmps=[]
for item in reversed(['奴隶社会', '非洲', '古埃及文明', '金字塔']):
    tmp={item:[]}
    tmps.append(tmp)
    print(tmp)

print(tmps)

print('-'*99)

new_tmp=defaultdict(list)
new_tmp['奴隶社会'].append({'test':[]})
print(new_tmp)

tmp_key = '奴隶社会'
print(new_tmp[tmp_key][0])
tmp_dir_3 = {'d': []}
new_tmp[tmp_key][0]['test'].append(tmp_dir_3)


_item = new_tmp['奴隶社会']
_item = _item[0]
_item = _item['test']

print('rwerwer')
print(_item)

for i in range(len(tmps)-1):

    # print(tmps[i])



    for key,value in tmps[i+1].items():
        # print(key,end='   ')
        # print(value)
        tmp_key=key
    # print(tmp_key)
    # print(tmps[i+1])
    # new_tmp[i+1][tmp_key].append(tmps[i])
    # print('-'*55)
    # print(new_tmp)


print(new_tmp)
print('-'*99)


# def add_dic(dic_item,item):
#     if isinstance(dic_item, dict):
#         add_dic(dic_item)
#
#     for k,v in dic_item.items():
#         if k==item:
#             dic_item.append({item:[]})
#         else:
#

# json_dic={
#     "奴隶社会": [{
#         "非洲": []
#     }, {
#         "亚洲": [{
#             "古印度": []
#         }]
#     }, {
#         "欧洲": []
#     }]
# }
# print(json.dumps(json_dic,ensure_ascii=False,indent=4))

insert_item = {"a": []}
def insert_end(dict_in,item):
    for k,v in dict_in.items():
        if isinstance(v,list) and len(v)==0:
            dict_in[item]=[]
        else:
            _dict=dict_in[v][0]
            insert_end(_dict,item)

print(insert_item)
insert_end(insert_item,'b')
print(insert_item)




print('-'*99)



p={'奴隶社会': [{'test': [{'d': []}]}]}
print(p)

for k,v in p.items():
    print(k)
    print(v)

# print(p['奴隶社会'])
# print(p['奴隶社会'][0]['test'])
# print(type(p['奴隶社会'][0]['test'][0]['d']))



print('-'*99)

p={}
test='---'
p[test]='1212'
print(p)

















