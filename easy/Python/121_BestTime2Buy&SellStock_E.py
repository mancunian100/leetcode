class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit, profit, minPrice = 0, 0, float('Inf')
        
        if len(prices) < 2:
            return 0
        
        for i in prices:
            if i < minPrice:
                minPrice = i
            else:
                profit = i - minPrice
                if profit > maxProfit:
                    maxProfit = profit 
        return maxProfit