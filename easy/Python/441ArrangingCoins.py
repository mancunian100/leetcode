# class Solution:
#     def arrangeCoins(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         # 不知为什么牛顿法在n=8时莫名出问题
#         t = 0
#         while (t**2 + t)/2 - n != 0:
#             t -= ((t**2 + t)/2-n)/(t+0.5)
#         return int(t)

class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(((n*8+1)**0.5-1)/2)