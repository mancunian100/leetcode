class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 很啰嗦的牛顿法
        dct = {}
        if num == 0:
            return True
        if num == 1:
            return True
        x = num // 2
        while x**2 != num:
            x += num / (2*x) - x / 2
            x = int(x)
            if x == 0:
                return False
            if x not in dct.keys():
                dct[x] = 1
            else:
                return False
        return True