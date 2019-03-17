################## 140ms 22% ################
# class Solution:
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         for i in range(0,k):
#             m = nums[-1]
#             nums.pop(-1)
#             nums.insert(0,m)

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums = nums[0-k:] + nums[:0-k]
        print(nums)

nums = [1,2,3,4,5,6,7]
k = 3
Solution().rotate(nums, k)
print(nums)