class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 借鉴别人的思想：去掉不想等的一对数，最后剩下的数返回
        count = 0
        pair = nums[0]
        for i in nums:
            if i == pair:
                count += 1
            else:
                count -= 1
                if count == 0:
                    pair = i
                    count = 1
        if count > 0:
            return pair