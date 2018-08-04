class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        sig = 1
        if x < 0:
            sig = -1
            x = -x
        while x:
            temp = x % 10
            x //= 10
            result = result * 10 + temp
        if x > 2**31 or x < -2**31:
            return 0
        if result > 2**31 or result < -2**31:
            return 0
        return result * sig