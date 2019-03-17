class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 从第二个开始，与第计数器（计数器从0，即第一个开始）个进行相邻元素的对比，不同的就覆盖式记录，计数器加一，相同不记录，计数器不变
        l = len(nums)
        if l == 0:
            return 0
        index = 0
        for i in range(1, l):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]
                
        return index + 1