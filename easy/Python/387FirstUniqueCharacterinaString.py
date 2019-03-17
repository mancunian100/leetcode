class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 使用dict记录元素的索引，重复的就记作inf，最后取最小值，并判断一下
        l = len(s)
        if l == 0:
            return -1
        if l == 1:
            return 0
        dct = {}
        for i in range(l):
            if s[i] not in dct.keys():
                dct[s[i]] = i
            else:
                dct[s[i]] = float('inf')
        if min(dct.values()) == float('inf'):
            return -1
        else:
            return min(dct.values())