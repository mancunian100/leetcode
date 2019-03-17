class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 最多只能有两个负数，因此可以比较两个最小的数与最大的数相乘，还有最大的3个数相乘的结果
        nums.sort()
        return max(nums[0]* nums[1] * nums[-1], nums[-3] * nums[-2] * nums[-1])