class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 用dict做的，应该不符合不增加额外空间的要求
        dct = {}
        for i in range(len(nums)):
            dct[i+1] = i+1
        for i in nums:
            if i in dct:
                del dct[i]
        return list(dct.keys())