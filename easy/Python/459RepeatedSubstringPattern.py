class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 若遇到与第一个元素相同的就切片，看成倍数后是否与s相同
        l = len(s)
        if l == 1:
            return False
        for i in range(1, l):
            if s[i] == s[0]:
                if l % i != 0:
                    pass
                elif s[:i] * (l//i) == s:
                    return True
        return False