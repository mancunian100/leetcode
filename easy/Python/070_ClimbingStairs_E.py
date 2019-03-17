class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        n1 = 1
        n2 = 2

        if n == 1:
            return n1
        elif n == 2:
            return n2
        else: 
            while(n-2):
                n3 = n1 + n2
                n1 = n2
                n2 = n3
                n -= 1
        return n3

n = 4
re = Solution().climbStairs(n)
print(re)