from collections import deque

all_image = deque()

all_image.append('a')
all_image.append('b')
all_image.append('c')

all_image.appendleft('1')
all_image.appendleft('2')
all_image.appendleft('3')

print(all_image)
# deque(['3', '2', '1', 'a', 'b', 'c'])


while all_image:
    img = all_image.pop()
    print(img)
# c
# b
# a
# 1
# 2
# 3


print(all_image)
# deque([])
