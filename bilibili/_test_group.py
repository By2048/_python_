import math

list=[i for i in range(20)]
print(list)


setp=10


for i in range(0,len(list),setp):
    print(list[i:i+setp])
