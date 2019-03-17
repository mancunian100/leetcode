class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        l = len(s)
        for i in s:
            d = ord(i) - ord('A') + 1
            d = d*26**(l-1)
            result += d
            l -= 1
        return result