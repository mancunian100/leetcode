class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ''
        while n>0:
            s += chr((n-1)%26 + ord('A'))     # ord(x) return ASCII of x
            n = (n-1)//26                     # 除以并取商的整数部分
        return s[::-1]