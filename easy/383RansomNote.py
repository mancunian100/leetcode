class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # 使用dict记录magazine的字符
        dct = {}
        for i in magazine:
            if i not in dct.keys():
                dct[i] = 1
            else:
                dct[i] += 1
        for i in ransomNote:
            if i in dct.keys() and dct[i] > 0:
                dct[i] -= 1
            else:
                return False
        return True