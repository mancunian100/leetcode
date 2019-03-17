class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # NOTICE that the majority element always exist in the array,
        # so that the middle always is the answer
        return sorted(nums)[len(nums)//2]