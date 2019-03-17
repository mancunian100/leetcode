class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s) - 1
        result = 0
        for i in s:
            result += (ord(i)-64) * 26**l
            l -= 1
        return result