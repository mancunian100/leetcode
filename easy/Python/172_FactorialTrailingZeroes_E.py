class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 判断n中有多少5，25，125,......
        d = 5
        count = 0
        while n >= d:
            d *= 5
            count += 1
        
        re = 0
        while d > 5:
            re += n // (d//5) 
            d = d//5
        return re