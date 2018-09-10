# 一开始想的复杂化法，很慢很慢
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        
        v = ''
        for i in s[::-1]:
            if i in vowels:
                v += i
                
        count = 0
        for i in range(0, len(s)):
            if s[i] in vowels:
                s = s[0:i] + v[count] + s[i+1:]
                count += 1
        return s

# 利用双指针
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return s
        s1 = list(s)
        p1, p2 = 0, len(s)-1
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        while p1 < p2:
            while p1 < p2 and s1[p1] not in vowels:
                p1 += 1
            while p1 < p2 and s1[p2] not in vowels:
                p2 -= 1
            s1[p1], s1[p2] = s1[p2], s1[p1]
            p1 += 1 # 这步与下步是容易遗漏的，即交换后也要移位要不然while死循环
            p2 -= 1
        return ''.join(s1)