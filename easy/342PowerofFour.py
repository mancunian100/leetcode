class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 同样的方法
        while num > 0 and not (num % 4):
            num /= 4
        return num == 1