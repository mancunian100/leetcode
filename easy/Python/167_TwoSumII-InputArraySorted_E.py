class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0 
        j = len(numbers) - 1
        
        while i < j:
            add = numbers[i]+numbers[j]
            if add == target:
                return [i+1,j+1]
            elif add > target:
                j -= 1
            else:
                i += 1