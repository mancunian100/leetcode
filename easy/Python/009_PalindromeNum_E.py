class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        sx = str(x)
        if sx == sx[::-1]:
            return True
        else:
            return False