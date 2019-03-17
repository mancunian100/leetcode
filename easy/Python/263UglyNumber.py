class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 就是无脑除以2，3，5，最后判断余数是不是1
        if num < 1:
            return False
        while not num % 2:
            num /= 2
        while not num % 3:
            num /= 3
        while not num % 5:
            num /= 5
        if num == 1:
            return True
        else:
            return False