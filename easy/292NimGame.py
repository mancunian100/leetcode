class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 两轮的数字总可以凑成4，而把4留给对手就会赢
        return bool(n % 4)