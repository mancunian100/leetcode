# 原题说会有很多次调用sumRange函数，所以可以将大量工作放在__init__函数中，下面这种无脑解法就非常低效了
class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nlist = nums
        
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nlist[i:j]) + self.nlist[j]
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

# 高效解法：
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # 为了快速调用函数，可以转化求和为做差，即s[j]-s[i-1]，i需要分类是否大于零
        self.s = []
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            self.s.append(temp)
            
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        l = len(self.s)
        if j >= l:
            j = l-1
        if i <= 0:
            return self.s[j]
        else:
            return self.s[j] - self.s[i-1]