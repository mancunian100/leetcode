class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        result = 0
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        for i in dic:
            if dic[i]%2:
                result = 1
            dic[i] = dic[i]//2
               
        if 0 in dic.values():
            result = 1
            
        result += 2*sum(dic.values())
        return result
        