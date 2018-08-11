class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 只要前面的子数组大于零就应该考虑记录下来，避免后面有可以更大的情况（而不是只把第i项大于零的记录下来，那样有可能漏掉后面更大的数）
        # loc记录动态的最大，glo把loc出现过的最大记录下来
        l = len(nums)
        if l == 0:
            return 0
        loc = nums[0]
        glo = nums[0]
        for i in nums[1:]:
            if loc < 0:
                loc = i
            else:
                loc += i
            glo = max(loc, glo)
        return glo