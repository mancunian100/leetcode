class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # 使用dict记录出现的次数
        dct = {}
        for i in s:
            if i not in dct.keys():
                dct[i] = 1
            else:
                dct[i] += 1
        for i in t:
            if i not in dct.keys():
                return i
            elif i in dct.keys() and dct[i] > 0:
                dct[i] -= 1
            else:
                return i