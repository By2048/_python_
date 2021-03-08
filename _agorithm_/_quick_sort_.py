import random

"""
1.选定Pivot中心轴 (随机
    特殊情况下 数组由小到大排列 选取第一个为Pivot 有性能问题
2.将大于Pivot的数字放在Pivot的右边
3.将小于Pivot的数字放在Pivot的左边
4.分别对左右子序列重复前三步操作
"""


def quick_sort_1(data, l, r):
    if l >= r:
        return

    left = l
    right = r
    pivot = data[left]

    while left < right:

        while left < right and data[right] >= pivot:
            right -= 1
        if left < right:
            data[left] = data[right]

        while left < right and data[left] <= pivot:
            left += 1
        if left < right:
            data[right] = data[left]

        if left >= right:
            data[left] = pivot

    quick_sort_1(data, l, left - 1)
    quick_sort_1(data, right + 1, r)


def quick_sort_2(data):
    """Sort the array by using quicksort."""

    less = []
    equal = []
    greater = []

    if len(data) > 1:
        pivot = data[0]
        for x in data:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quick_sort_2(less) + equal + quick_sort_2(greater)
    else:
        return data


def test_1():
    data = [random.randint(1, 100) for _ in range(30)]
    print(" ".join([str(item) for item in data]))
    quick_sort_1(data, 0, len(data) - 1)
    print(" ".join([str(item) for item in data]))


def test_2():
    data = [random.randint(1, 100) for _ in range(30)]
    print(" ".join([str(item) for item in data]))
    data = quick_sort_2(data)
    print(" ".join([str(item) for item in data]))


if __name__ == '__main__':
    test_1()
    test_2()
