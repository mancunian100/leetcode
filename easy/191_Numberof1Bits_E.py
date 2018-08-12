class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = bin(n)
        count = 0
        for i in b[2:]:
            if i == '1':
                count += 1
        return count