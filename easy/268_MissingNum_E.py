class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        x = sum(nums)
        
        d = x - (n-1)*n//2
        return n-d