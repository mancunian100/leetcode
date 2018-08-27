class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        if num < 0:
            num = num + 2**32
        
        x = ''
        while num:
            a = num % 16
            if a > 9:
                a = a - 10 + ord('a')
                x = chr(a) + x
            else:
                x = str(a) + x
            num = num // 16
            
        return x
            