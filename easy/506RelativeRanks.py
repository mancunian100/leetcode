class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # 先复制一个nums1，排序，将顺序记录在dct中，注意把nums1的值作为keys
        # 再在原nums中用dct中的顺序替换每个nums的值，再处理为str
        l = len(nums)
        dct = {}
        nums1 = nums[:]
        nums1.sort(reverse=True)
        for i in range(l):
            dct[nums1[i]] = i
        for i in range(l):
            nums[i] = dct[nums[i]] + 1
            if nums[i] == 1:
                nums[i] = 'Gold Medal'
            if nums[i] == 2:
                nums[i] = 'Silver Medal'
            if nums[i] == 3:
                nums[i] = 'Bronze Medal'
            else:
                nums[i] = str(nums[i])
        return nums