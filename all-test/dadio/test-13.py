# 找到斐波那契数的最后一位数字


def change_num(in_num):
    if in_num < 10:
        return in_num
    else:
        return int(str(in_num)[-1])


def get_last_digit(index):
    if index <= 0:
        return 0
    if index == 1 or index == 2:
        return 1
    perPer = 1
    per = 1
    curent = 2
    for i in range(3, index + 1, 1):
        curent = perPer + per
        perPer = per
        per = curent

        curent=change_num(curent)
        perPer=change_num(perPer)
        per=change_num(per)


    return curent


# print(list(str(get_last_digit(193150)))[-1])

get_last_digit(193150)

# print(change_num(5))
# print(change_num(15))
# print(change_num(100))
