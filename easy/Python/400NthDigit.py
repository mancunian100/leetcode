class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 判断多少位的数，再根据位数处理
        c0 = 0
        t = 0
        while t < n:
            t += 9 * 10**c0 * (c0+1)
            c0 += 1
        temp = c0 - 1
        while temp:
            n -= 9 * 10**(temp-1) * temp
            temp -= 1
        num = n // c0 + 10**(c0-1) - 1
        if not n % c0:
            return int(str(num)[-1])
        else:
            return int(str(num+1)[n%c0-1])