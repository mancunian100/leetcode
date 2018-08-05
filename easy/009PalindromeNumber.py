class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # reverse x and compare it with x
        reverse = 0
        y = x
        if x < 0:
            return False
        while y:
            temp = y % 10
            reverse = reverse * 10 + temp
            y //= 10
        return reverse == x