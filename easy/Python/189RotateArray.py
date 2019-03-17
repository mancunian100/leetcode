class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 偷懒使用数组的切片，应该要用更基础的算法去实现，最后nums[:]不加:会出问题
        l = len(nums)
        if l == 0:
            return None
        k %= l
        nums[:] = nums[-k:] + nums[:-k]