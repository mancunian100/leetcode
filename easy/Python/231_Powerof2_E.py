class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        x = 1
        while x < n:
            x *= 2
            if x == n:
                return True
        return False
            
        
            