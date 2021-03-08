import random

"""
1.选定Pivot中心轴 (随机
    特殊情况下 数组由小到大排列 选取第一个为Pivot 有性能问题
2.将大于Pivot的数字放在Pivot的右边
3.将小于Pivot的数字放在Pivot的左边
4.分别对左右子序列重复前三步操作
"""

data = [random.randint(1, 100) for _ in range(30)]


def quick_sort(data, l, r):
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

    quick_sort(data, l, left - 1)
    quick_sort(data, right + 1, r)


if __name__ == '__main__':
    print()
    print(" ".join([str(item) for item in data]))
    quick_sort(data, 0, len(data) - 1)
    print(" ".join([str(item) for item in data]))
    print()
