import os

class X:
    pass

print(X.__class__)
print(X.__class__.__base__)

print(help(os.path))


'abc'.upper()
'ABC'


print('---|-')




str = input('选择需要重命名的项。。。\n\n')
if str=='0':
    print('0')
if str=='.':
    print('all')
nums = str[:]
print(type(nums))
