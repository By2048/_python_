# 请你来实现抽奖


def get_luck_num(name,weight):
    luck_num = 0
    luck_num += len(name)
    for item in list(name):
        luck_num += ord(str.lower(item)) - 96
    luck_num *= weight
    # print(luck_num)
    return luck_num

num_info = [i for i in range(1, 26 + 1)]
chr_info = [chr(i) for i in range(97, 123)]


def rank(name_str, weights, n):
    names=[item for item in name_str.split(',')]
    if name_str=='':
        return 'No participants'
    if n>len(names):
        return 'Not enough participants'
    info_dirs = {}
    for (name, weight) in zip(names, weights):
        info_dirs[name]=[get_luck_num(name,weight),weight]
    info_dirs=sorted(info_dirs.items(),key=lambda x:(-1*x[1][0],x[0]))
    # print(info_dirs)
    return info_dirs[n-1][0]


print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4))#, "Benjamin"))
# print(rank("Lagon,Lily", [1, 5], 2))#, "Lagon")
# print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 8))#, "Not enough participants")
# print(rank("", [4, 2, 1, 4, 3, 1, 2], 6))#, "No participants")