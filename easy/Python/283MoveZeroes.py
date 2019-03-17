class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # for循环用来计数过了多少个元素，count用来计有多少非零元素
        count = 0
        for i in range(len(nums)):
            if nums[count] == 0:
                del(nums[count])
                nums.append(0)
            else:
                count += 1