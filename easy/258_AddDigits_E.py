class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        add = 0
        for i in str(num):
            add += int(i)
        if len(str(add)) == 1:
            return add
        return self.addDigits(add)
        