class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a,b = list(s),list(t)
        a.sort()
        b.sort()
        return a == b
        
        