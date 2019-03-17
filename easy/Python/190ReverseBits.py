class Solution:
    # @param n, an integer
    # @return an integer
    # 这里是位运算，其实就是把n的最后一位一个一个地填在result的最后一位
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            result = (result << 1) + (n & 1)
            n >>= 1
        return result