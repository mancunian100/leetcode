class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 把每一次上涨的值都记录下来
        result = 0
        l = len(prices)
        if l < 2:
            return result
        for i in range(1, l):
            result += max(0, prices[i] - prices[i-1])
        return result