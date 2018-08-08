class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 将原数组写成整数，加一后还原成数组
        num = 0
        result = []
        if len(digits) == 0:
            return 1
        for i in digits:
            num = num * 10 + i
        num += 1
        while num:
            result.insert(0, num % 10)
            num //= 10
        return result