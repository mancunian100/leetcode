class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 同样使用计数器，找到大于等于target的元素就返回，或者循环结束了也返回
        index = 0
        for i in nums:
            if nums[index] < target:
                index += 1
            else:
                return index
        return index