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


from _datetime import datetime



if __name__ == '__main__':
    now = datetime.today()
    print(now.year)
    print(now.month)
    print(now.day)

    da="20170317"
    print(da[0:4]+'-'+da[4:6]+'-'+da[6:8])

