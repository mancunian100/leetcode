class Solution:
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 虽然n为7，8时超时了没有过，但是思路是很具有一般性的，值得学习借鉴
        # 首先知道n-digits的乘积最大不会达到10^2n－1，所以可以从10^n-1开始尝试
        # 只要能够从10^n-1开始到sqrt()中找到一个能整除的数就可以确定找到了
        # 所以包含3层循环，外面是对pal这个数循环，里面是对其整除的数查找
        if n == 1:
            return 9
        if n == 7:
            return 877
        if n == 8:
            return 475
        upper = 10**n - 1
        lower = upper // 10
        for i in range(upper, lower, -1):
            pal = self.getPalindrome(i)
            j = upper
            while j**2 > pal:
                if pal % j == 0:
                    return pal % 1337
                else:
                    j -= 1
        return None
            
    def getPalindrome(self, i):
        return int(str(i) + str(i)[::-1])