class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 注意奇数个的可以取出偶数个来组
        dct = {}
        result = 0
        for i in s:
            if i not in dct.keys():
                dct[i] = 1
            else:
                dct[i] += 1
        odd = 0
        for i in dct.values():
            if i % 2 == 0:
                result += i
            else:
                odd = 1
                result += i - 1
        return result + odd