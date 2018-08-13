class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 就是不断除以3，最后是1就返回True，注意n为0时单独讨论
        if n == 0:
            return False
        while not n % 3:
            n /= 3
        return n == 1