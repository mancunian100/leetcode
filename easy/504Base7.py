class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 转换10进制为7进制
        result = ''
        sig = 1
        if num < 0:
            sig = -1
            num = -num
        if num == 0:
            return '0'
        while num:
            temp = num % 7
            result = str(temp) + result
            num //= 7
        if sig == -1:
            result = '-' + result
        return result