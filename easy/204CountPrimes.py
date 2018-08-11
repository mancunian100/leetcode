class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 筛法，注意筛选的条件，是把i**2的数去掉，并且从2开始
        if n <= 2:
            return 0
        result = [True] * n
        result[0] = result[1] = False
        for i in range(2, int(n**0.5) + 1):
            if result[i]:
                result[i*i: n: i] = [False] * len(result[i*i: n: i])
        return sum(result)