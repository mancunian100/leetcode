class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # 先判断15的倍数，再是3和5
        result = []
        for i in range(n):
            t = i+1
            if t % 15 == 0:
                result.append('FizzBuzz')
            elif t % 3 == 0:
                result.append('Fizz')
            elif t % 5 == 0:
                result.append('Buzz')
            else:
                result.append('{}'.format(t))
        return result