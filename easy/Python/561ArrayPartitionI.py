class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 排序后按大小，最大的和最大的配对，最后求每一对相对小的值的和，也就是每隔一个数进行相加
        nums.sort()
        return sum(nums[::2])