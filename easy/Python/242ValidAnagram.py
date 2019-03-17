class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 使用dct记录每个字母出现的次数，对比两者是否相同
        dct = {}
        for i in s:
            if i not in dct.keys():
                dct[i] = 1
            else:
                dct[i] += 1
        for i in t:
            if i not in dct.keys():
                return False
            else:
                dct[i] -= 1
                if dct[i] < 0:
                    return False
        if sum(dct.values()) == 0:
            return True
        else:
            return False

# 等价方法，字典可以直接进行对比
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dct_s, dct_t = {}, {}
        for i in s:
            if i not in dct_s.keys():
                dct_s[i] = 1
            else:
                dct_s[i] += 1
        for i in t:
            if i not in dct_t.keys():
                dct_t[i] = 1
            else:
                dct_t[i] += 1
        if dct_s == dct_t:
            return True
        else:
            return False