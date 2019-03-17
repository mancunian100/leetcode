class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 判断在转换时是否和之前的记录重复
        record = [n]
        while n != 1:
            n = self.trans(n)
            if n in record:
                return False
            else:
                record.append(n)
        return True
        
    def trans(self, x):
        """
        return the sum of squares of its digits
        """
        s = 0
        while x:
            temp = x % 10
            s += temp**2
            x //= 10
        return s