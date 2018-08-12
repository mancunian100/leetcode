class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 两层循环
        while num // 10 > 0:
            s = 0
            while num:
                s += (num % 10)
                num //= 10
            num = s
        return num
            