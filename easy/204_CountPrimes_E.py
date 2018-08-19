class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 厄拉多塞筛法，判断到n**0.5就可以了，之后未去掉的一定是素数
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)



# ############### Time limit exceeded when n > 1 000 000 ################
# class Solution:
#     def countPrimes(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n <= 2:
#             return 0
#         elif n < 10:
#             return n//2
#         else:
#             prList = [2,3,5,7]
#             for i in range(10, n):
#                 if self.isPrime(i, prList):
#                     prList.append(i)
                    
#         return len(prList)
                    
#     # 数论：不在6倍数两侧的一定不是质数。剩下的判断是否能除尽之前的质数，判断到sqrt(n)为止
#     def isPrime(self, n, prList):
#         if n%6 != 1 and n%6 != 5:
#             return False
#         else:
#             trymax = n**0.5
#             for i in prList:
#                 if i > trymax:
#                     break
#                 else:
#                     if n%i == 0:
#                         return False
#             return True