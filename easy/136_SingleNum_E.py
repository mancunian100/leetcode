################## 1500ms 3% ####################
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 新建一个数组，将nums中的数字添加进去，如果已经存在就删除这个数，最后剩下独有的数
        newnums = []
        for i in nums:
            if i in newnums:
                newnums.remove(i)
            else:
                newnums.append(i)
        return newnums[0]

################## 40ms 99% ####################
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Math: 2*(a+b+c)-(a+a+b+b+c) = c
        return 2 * sum(set(nums)) - sum(nums)

nums = [1,0,1]
print(Solution().singleNumber(nums))