class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 最直接，很慢的方法
        result = ''
        for i in s:
            result = i + result
        return result