class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 还是需要使用dict才能满足时间要求，写完发现两句相同的语句可以合并成一个逻辑
        l = len(nums)
        if l < 2 or k < 1:
            return False
        dct = {}
        for i in range(len(nums)):
            if nums[i] not in dct:
                dct[nums[i]] = i
            elif i - dct[nums[i]] <= k:
                return True
            else:
                dct[nums[i]] = i
        return False