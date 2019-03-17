class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # 直接法，注意分类，要分成4种情况
        s = str.split()
        dct = {}
        if len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dct.keys() and s[i] not in dct.values():
                dct[pattern[i]] = s[i]
            elif pattern[i] not in dct.keys() and s[i] in dct.values():
                return False
            elif dct[pattern[i]] != s[i]:
                return False
            else:
                pass
        return True