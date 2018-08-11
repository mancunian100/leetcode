class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 递推的思路，第k次的方案可以分为第一步是1还是2分为2种，1就是第k-1次的方案数量，2就是k-2的方案数量
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            f1 = 1
            f2 = 2
            for i in range(2, n):
                f1, f2 = f2, f1+f2
            return f2