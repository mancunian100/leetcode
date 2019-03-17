class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = bin(n)[2:]
        while len(b) < 32:
            b = '0'+b
        newb = b[::-1]
        newn = int(newb, 2)

        print(n, b , newb, newn)
        

n = 43261596
Solution().reverseBits(n)

