class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        ## 二分法，注意选区左边界和右边界时由于是向下取整，所以判断条件两边的等号不一样
        # if x == 1:
        #     return 1
        # xl = 0
        # xr = x
        # x2 = (xl + xr) // 2
        # while x < x2**2 or x >= (x2+1)**2:
        #     if x < x2**2:
        #         xr = x2
        #         x2 = (xl + xr) // 2
        #     else:
        #         xl = x2
        #         x2 = (xl + xr) // 2
        # return x2

        # newton method
        # 先把f(x)=0的方程写出来
        # 注意判断条件会对结果有影响
        # 最后的取整根据题目要求来
        if x == 0:
            return 0
        t = x
        while (t - x/t) / 2 >= 1e-5:
            t = (t + x/t) / 2
        return int(t)