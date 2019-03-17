class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mysum = 0
        mem = set()
        while mysum != 1:
            for i in str(n):
                mysum += int(i)**2
            n = mysum
            mysum = 0
            if n in mem:
                return False
            elif n == 1:
                return True
            else:
                mem.add(n)