class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 最简便的思路：只需要知道有多少5进行了乘法就有多少0，因为每有一个5至少会有一个2进行乘法
        count = 0
        while n:
            n //= 5
            count += n
        return count