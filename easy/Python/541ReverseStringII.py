class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # 使用python的高级函数
        if k == 1:
            return s
        s = list(s)
        l = len(s)
        for i in range(0, l, 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return ''.join(s)
            