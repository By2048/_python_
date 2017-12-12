# 找到第一个非连续的数字

def first_non_consecutive(arr):
    for i in range(len(arr)-1):
        if arr[i+1]-arr[i]!=1:
            return arr[i+1]
    return None



print(first_non_consecutive([1,2,3,4,6,7,8]))#, 6))
print(first_non_consecutive([1,2,3,4,5,6,7,8]))#, None))
print(first_non_consecutive([4,6,7,8,9,11]))#, 6))
print(first_non_consecutive([4,5,6,7,8,9,11]))#, 11))
print(first_non_consecutive([31,32]))#, None))
print(first_non_consecutive([-3,-2,0,1]))#, 0))
print(first_non_consecutive([-5,-4,-3,-1]))#, -1))


# test1=[1,2,3,4,6,7,8]
# print(first_non_consecutive(test1))