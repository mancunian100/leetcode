class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
#         stair = 1
#         x = 1
#         while x < n:
#             stair += 1
#             x += stair
        
#         return stair-1 if x - n > 0 else stair
    
        return int(((1+8*n)**0.5 - 1 )/ 2)

            
        