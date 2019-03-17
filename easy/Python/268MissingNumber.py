class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 因为已知只缺少一个数，所以可以用求和公式知道总和，再减去数组的总和
        l = len(nums)
        s = 0
        for i in nums:
            s += i
        return int((l**2 + l) / 2 - s)