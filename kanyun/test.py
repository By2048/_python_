import json

# Python 字典类型转换为 JSON 对象
data = {
    'no' : 1,
    'name' : ['Runoob'],
    'url' : 'http://www.runoob.com'
}



json_str = json.dumps(data)

print (json_str)

data = json.loads(json_str)

print ("data2['name']: ", data['name'])
print ("data2['url']: ", data['url'])

data['name']+=['qqqqqqqqqqqqqq']

print ("data2['name']: ", data['name'])


data["rwerwe"]='77777777'


def my_join(lists):
    path=''
    for list in lists[:-1]:
        path+=list+'\\'
    path+=lists[len(lists)-1]
    return path

ll=['1','2','3','4','5']
print(ll)
ll.pop()
print(ll)

# print(ll[:-1])
# print(ll[-1:])
# print(my_join(ll))

# i='4'
# if i in ['1','2','3','4','5']:
#     print('true')
# else:
#     print('false')

p1=['c-sharp']
p2=['c-sharp', 'c-sharp.md']
p3=['c-sharp', '使用JObject解析Json.md']

item='c-sharp.md'
print(item[:-3])
print(type(item[:-3]))

#
# def is_equal(list):
#     if len(list)==1:
#         return False
#     item1=list[-1]
#     item2=list[-2]
#     if item1[:-3]==item2:
#         return True
#     else:
#         return False
#
# print(is_equal(p1))