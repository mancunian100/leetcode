################### 84ms ################
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        if nums == []:
            return 0
        pre = nums[0]
        for i in nums[1:]:
            if i != pre:
                nums[count] = i
                count += 1
            pre = i
        return count

################## 700ms ###############
# class Solution:
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if nums == []:
#             return 0
#         pre = nums[0]
#         for i in nums[1:]:
#             if not i - pre:
#                 nums.remove(i)
#             pre = i
#         return len(nums)