class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 取负法：既然nums元素在[1,n]之间，又下标是[0,n-1]之间，因此对nums减1，然后作为下标取负
        # 最后没取负的就是缺少的元素
        for i in nums:
            index = abs(i) - 1
            nums[index] = -abs(nums[index])
        
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]