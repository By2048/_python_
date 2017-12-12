
def solve(a, b):
    if a>=2:
        a=a-1
    all_pri_list = []
    for i in range(100):
        for j in range(100):
            if i>=j:
                all_pri_list.append((i, j))
            else:
                all_pri_list.append((j, i))
    for item in all_pri_list:
        print(item)
    print(len(all_pri_list))
    test=set(all_pri_list)
    print(len(test))
solve(100,200)


a=[1,2]