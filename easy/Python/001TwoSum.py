class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 使用dict实现哈希表的功能
        tmp = {}
        for i in range(len(nums)):
            if target - nums[i] in tmp:
                return [tmp[target-nums[i]], i]
            else:
                tmp[nums[i]] = i