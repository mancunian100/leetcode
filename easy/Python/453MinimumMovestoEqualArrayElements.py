class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 法一：给n-1个数字加1，相当于给剩余的那个数字减1
        # 因此，等效于不断减每个值，直至全部达到所有元素中的最小值
        m = min(nums)
        s = 0
        for i in nums:
            s += i - m
        return s