# AND 从左到右扫描，返回第一个为假的表达式值，无假值则返回最后一个表达式值。
print('a' and 'b')
print({} and 'b')
print('a' and 'b' and 'c')
print()

# OR 从左到右扫描，返回第一个为真的表达式值，无真值则返回最后一个表达式值。
print('a' or 'b')
print('' or 'b')
print('' or [] or {})
print()

# and or搭配
print(1 and 'a' or 'b')
print(0 and 'a' or 'b')
