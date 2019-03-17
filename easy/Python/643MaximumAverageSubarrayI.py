class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # 还是用loc和glo记录中途的局部值和全局最大值
        loc = glo = sum(nums[:k])
        for i in range(1,len(nums)-k+1):
            loc += nums[i+k-1] - nums[i-1]
            if loc > glo:
                glo = loc
        return glo/k