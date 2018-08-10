class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = -x
            x = str(x)
            rx = x[::-1]
            rx = int(rx)
            if -rx < -2147483648:
                return 0
            return -rx
        else:
            x = str(x)
            rx = x[::-1]
            rx = int(rx)
            if rx > 2147483647:
                return 0
            return rx