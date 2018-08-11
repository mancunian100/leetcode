class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #  注意在dct中没有s[i]时要使用dct.keys()来检查keys中有没有这个值，分为4类情况
        dct = {}
        l = len(s)
        for i in range(l):
            if s[i] not in dct.keys() and t[i] not in dct.values():
                dct[s[i]] = t[i]
            elif s[i] not in dct.keys() and t[i] in dct.values():
                return False
            elif dct[s[i]] != t[i]:
                return False
            else:
                pass
        return True