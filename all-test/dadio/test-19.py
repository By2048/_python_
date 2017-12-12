import math


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_prime(a,b):
    primes=[]
    for i in range(a,b):
        if is_prime(i):
            primes.append(i)
    return primes


top_10000_prime=get_prime(1,10000)



def solve(a, b):
    if a>=2:
        a=a-1
    pri_list = get_prime(a,b)
    all_pri_list = set()
    for i in pri_list:
        for j in pri_list:
            if i>=j:
                all_pri_list.add((i, j))
            else:
                all_pri_list.add((j, i))


    # for item in all_pri_list:
    #     print(item)
    print(list(set(all_pri_list)))
    # #
    # print(all_pri_list)



    cnt = 0
    for item in all_pri_list:

        _i = item[0]
        _j = item[1]

        tmp = _i * _j
        if tmp<10:
            continue
        # print(tmp)
        nums = [_item for _item in list(str(tmp))]
        # print(nums)
        sum_num = 0
        for num in nums:
            sum_num += int(num)

        if sum_num in top_10000_prime :
            # print('----------------------prime ')
            cnt += 1

    return cnt


print(solve(2000,5000))

# print(top_10000_prime)
