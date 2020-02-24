import json

data = {
    'a': 1,
    'b': {
        'c': 2,
        'd': 3,
        'e': {'f': 4}
    },
    'c': [1, 2, 3, 4],
    'd': {
        'e': [1, 2, 3, 4]
    },
    'g': {'h': 5},
    'i': 6,
    'j': {'k': {'l': {'m': 8}}}
}


def test1(data):
    def echo(data):
        if isinstance(data, dict):
            for key, value in data.items():
                yield key, value
        elif isinstance(data, list):
            for index, value in enumerate(data):
                yield index, value

    for key, value in echo(data):
        if isinstance(value, (dict, list)):
            for _key, _value in test1(value):
                _key = f'{key}_{_key}'
                yield _key, _value
        else:
            yield key, value


result = {k: v for k, v in test1(data)}
print(json.dumps(result, indent=4))

#
# def test2(data):
#     for key, value in data.items():
#         if isinstance(value, (dict, list)):
#             for _key, _value in test1(value):
#                 _key = f'{key}_{_key}'
#                 yield _key, _value
#         elif isinstance(data, dict):
#         else:
#             yield key, value
#
#
# result = {k: v for k, v in test1(data)}
# print(json.dumps(result, indent=4))
