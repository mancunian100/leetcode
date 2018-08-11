class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 用min_val记录循环中遇到的局部最小值，loc记录每一次与局部最小值相减的利润，glo记录loc中最大的利润
        if len(prices) < 2:
            return 0
        loc, glo = 0, 0
        min_val = prices[0]
        for i in range(1, len(prices)):
            min_val = min(min_val, prices[i-1])
            loc = prices[i] - min_val
            glo = max(loc, glo)
        return glo