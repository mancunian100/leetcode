class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.oneWay(s,t) and self.oneWay(t,s)

    def oneWay(self, s, t):
        dic = {}
        for i in range(0, len(s)):
            if s[i] not in dic:
                dic[s[i]] = t[i] 
            else:
                if dic[s[i]] != t[i]:
                    return False
        return True
        
        