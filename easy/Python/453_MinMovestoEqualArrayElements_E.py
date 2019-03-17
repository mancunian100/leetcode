class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 给n-1个数字加1，相当于给剩余的那个数字减1，因此，等效于不断减每个值，
        # 直至全部达到所有元素中的最小值
        n0 = min(nums)
        re = 0
        for i in nums:
            re += i-n0
            
        return re