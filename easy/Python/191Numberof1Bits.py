class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 同样是位运算，因为默认似乎是32位的二进制数，所以比较好做
        result = 0
        for i in range(32):
            if (n & 1):
                result += 1
            n >>= 1
        return result