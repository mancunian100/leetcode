# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 二分法，需要注意边界情况
        l, r = 0, n-1
        while l <= r:
            m = (l + r) // 2
            if isBadVersion(m) == False:
                l = m + 1
            else:
                r = m - 1
        return r + 1