class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        
        minPrice = prices[0]
        profit = 0
        for i in prices[1:]:
            if i > minPrice:
                profit += i - minPrice
            minPrice = i
        return profit