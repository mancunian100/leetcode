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
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)