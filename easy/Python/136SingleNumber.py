class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 使用数组操作
        result = []
        for i in nums:
            if i not in result:
                result.append(i)
            else:
                result.remove(i)
        return result[0]