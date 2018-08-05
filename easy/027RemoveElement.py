class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 同样使用计数器，当元素与val不同时计数器加一，并覆盖式记录在nums前面
        index = 0
        for i in nums:
            if i != val:
                nums[index] = i
                index += 1
        
        return index