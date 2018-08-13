class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 两个指针从两边开始走，遇到目标就交换，注意每次的条件更改
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        c1, c2 = 0, len(s) - 1
        while c1 < c2:
            while c1 < c2 and s[c1] not in vowels:
                c1 += 1
            while c1 < c2 and s[c2] not in vowels:
                c2 -= 1
            s[c1], s[c2] = s[c2], s[c1]
            c1 += 1
            c2 -= 1
        return ''.join(s)
                