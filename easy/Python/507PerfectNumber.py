class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 确定一个因数（非0）的时候可以同时把另一个与之相乘得到num的因数找到，一起加入s中，所以此时边界条件就变为i^2<num
        # 注意若i^2 == num，那么只能对i加一次，所以单独处理（似乎leetcode的测试数据没有针对这个问题）
        s = 1
        i = 2
        if num == 1:
            return False
        while i**2 < num:
            if num % i == 0:
                s += i + (num/i)
            i += 1
        if i**2 == num:
            s += i
        return s == num