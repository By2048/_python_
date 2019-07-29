# coding=utf-8
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for ii, i in enumerate(nums):
            for jj, j in enumerate(nums):
                if i + j == target:
                    if ii == jj:
                        pass
                    else:
                        return [ii, jj]


a = Solution()

aaa = [-3, 4, 3, 90]
bbb = 0
c = a.twoSum(aaa, bbb)
print(c)
