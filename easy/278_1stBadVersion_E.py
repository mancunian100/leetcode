# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        
        while end - start > 1: 
            if isBadVersion((start+end)//2):
                end = (start+end)//2
            else:
                start = (start+end)//2
        if isBadVersion(start):
            return start
        else:
            return end