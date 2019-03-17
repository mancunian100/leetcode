class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 每次都忘记空格后要跟一个非空格才能算是一个词
        result = 0
        l = len(s)
        if l == 0:
            return 0
        if s[0] != ' ':
            result += 1
        for i in range(l-1):
            if s[i] == ' ' and s[i+1] != ' ':
                result += 1
        return result