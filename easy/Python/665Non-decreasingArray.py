class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 再一次体会浅复制，多个同时赋值的细节差别
        # one和two代表2种能够解决问题的所有办法，如果执行后还是不对那就返回False 
        one, two = nums[:], nums[:]
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                one[i-1] = one[i]
                two[i] = two[i-1]
                break
        return self.check(one) or self.check(two)
    
    def check(self, arr):
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                return False
        return True