class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        loc, glo = 0, 0
        for i in nums:
            loc = loc*i + i
            glo = max(loc, glo)
        return glo