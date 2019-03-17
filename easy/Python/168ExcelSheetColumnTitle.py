class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 类似于转换为26进制，但是由于没有0的元素，所以进位时要特殊处理
        if n == 0:
            return None
        result = ''
        while n:
            temp = n % 26
            if temp == 0:
                temp = 'Z'
                n = n // 26 - 1
            else:
                temp = chr(temp+64)
                n //= 26
            result = temp + result
        return result