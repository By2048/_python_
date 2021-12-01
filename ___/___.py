import sys
import platform

print(1, sys.platform)
print(2, platform.system())
print()

print(3, 'example'.ljust(50, '_'))
print(4, 'example'.rjust(50, '_'))

# %%

print(123)

# list分组
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index in range(0, len(data), 3):
    item = data[index:index + 3]
    print(item)
