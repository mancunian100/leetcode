class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic = {}
        for i in magazine:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        for i in ransomNote:
            if i not in dic:
                return False
            
            dic[i] -= 1
            if dic[i] < 0:
                return False
        
        return True
                
        