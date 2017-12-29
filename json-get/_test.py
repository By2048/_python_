from collections import defaultdict

d = defaultdict(list)
d['sum'].append({'a': []})
d['sum'].append({'b': []})
d['sum'][0]['a'].append({'c': []})

print(d)
# defaultdict(<class 'list'>, {'sum': [{'a': [{'c': []}]}, {'b': []}]})


def search(d, key, default=None):
    """Return a value corresponding to the specified key in the (possibly
    nested) dictionary d. If there is no item with that key, return
    default.
    """
    stack = [iter(d.items())]
    while stack:
        for k, v in stack[-1]:
            if isinstance(v, dict):
                stack.append(iter(v.items()))
                break
            elif k == key:
                return v
        else:
            stack.pop()
    return default

print(search({"B": {"A": 2}}, "A"))




# {"奴隶社会": [{"非洲": []}, {"亚洲": []}, {"欧洲": []}]}

#
# print('--------------------------')
# test_item=[[i for i in range(4)]for j in range(4)]
# print(test_item)
#
# d=defaultdict(list)
# tmp_dir_0={'q':[]}
# tmp_dir_1={'w':[]}
# d['sum'].append(tmp_dir_0)
# d['sum'].append(tmp_dir_1)
# print(d)
#
# tmp_dir_2={'a':[]}
# tmp_dir_3={'b':[]}
#
# # d['sum']['q'].add(tmp_dir_2)
#
# print(d)
# # d['sum']['1'].append(tmp_dir_3)
#
# # for item in test_item:
# #     for i in range(len(item)-1,-1,-1):
# #         j=i
# #         tmp_dir={str(j),j}
# #         print('--')
# #         print(tmp_dir)
# #
# #         d['sum'].append(tmp_dir)
# # print(d)
#
#
#
#
#
#
# from collections import defaultdict
# foo = defaultdict(lambda: 10*defaultdict(list))
# foo['key1'][0].append('value')
# foo['key1'][1].append('other value')
# foo['key1'][2].append('other value')
# foo['key1'][0]['value'].append('fewfwe---')
#
# print(foo)
#
#
#
