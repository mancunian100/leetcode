class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 不是空格就对计数器加1
        # 若是空格，并且后一位不是空格（要求不是最后一位），那么计数器归零
        result = 0
        l = len(s)
        if l == 0:
            return result
        for i in range(l):
            if s[i] != ' ':
                result += 1
            elif i != l-1:
                if s[i+1] != ' ':
                    result = 0
        return result