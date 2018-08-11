class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划，还有些问题没想通，需要继续学习
        # dp[i]代表有i个家庭时的最大值，不是很理解为什么只有dp[i-2]能加上nums[i]，因为dp[i]不一定就包括了第i家的价值吧？
        l = len(nums)
        if l == 0:
            return 0
        elif l == 1:
            return nums[0]
        else:
            dp = [0 for i in range(l)]
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, l):
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])
            return dp[-1]