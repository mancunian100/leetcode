class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 注意0和负数，若是负数则表示补码，可以加上2**32处理为正数
        if num == 0:
            return '0'
        if num < 0:
            num += 2**32
        result = ''
        s = ['a', 'b', 'c', 'd', 'e', 'f']
        while num:
            temp = num % 16
            if temp > 9:
                temp = s[temp - 10]
            else:
                temp = str(temp)
            result = temp + result
            num //= 16
        return result