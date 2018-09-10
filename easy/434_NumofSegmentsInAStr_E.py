class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        v = 0
        
        if s == '':
            return 0
        if s[0] != ' ':
            result = 1
            
        for i in range(len(s)):
            if s[i] == ' ':
                v = 1
            if s[i] != ' ' and v == 1:
                result += 1
                v = 0
            
        return result