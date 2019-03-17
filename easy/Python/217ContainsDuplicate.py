class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 不使用set()函数，但是list又超时，似乎dict就可以满足时间要求
        if len(nums) == 1 or len(nums) == 0:
            return False
        dct = {}
        for i in nums:
            if i in dct.keys():
                return True
            else:
                dct[i] = True
        return False