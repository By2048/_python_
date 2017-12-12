# 组合一个新的数组

def unflatten(flat_array):
    out_arr = []
    index=0

    while index<len(flat_array):
        if flat_array[index] < 3:
            out_arr.append(flat_array[index])
        else:
            print()
            out_arr.append(flat_array[index:index+flat_array[index]])
            index+=flat_array[index]-1
        index+=1
    return out_arr


unflatten([3, 5, 2, 1])  # , [[ 3,5,2 ], 1 ])
unflatten([ 1, 4, 5, 2, 1, 2, 4, 5, 2, 6, 2, 3, 3 ])
# Test.assert_equals(unflatten([ 1, 4, 5, 2, 1, 2, 4, 5, 2, 6, 2, 3, 3 ]), [1, [4,5,2,1], 2, [4,5,2,6], 2, [3, 3] ])
