class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
                
        for i in t:
            if i not in dic:
                return i
            else:
                dic[i] -= 1
                if dic[i] < 0:
                    return i
        
        