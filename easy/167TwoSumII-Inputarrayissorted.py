class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 使用字典，利用排好序的特性
        dic = {}
        count = 1
        for i in numbers:
            if target - i in dic:
                return [dic[target - i], count]
            dic[i] = count
            count += 1