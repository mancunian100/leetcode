class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 不要忘记处理0
        if n == 0:
            return False
        while not (n % 2):
            n /= 2
        if n // 2 != 0:
            return False
        else:
            return True
        