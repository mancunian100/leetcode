class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = [float('-inf'), float('-inf'), float('-inf')]
        for i in nums:
            if i not in m:
                if i > m[0]: m = [i, m[0], m[1]]
                elif i > m[1]: m = [m[0], i, m[1]]
                elif i > m[2]: m = [m[0], m[1], i]
        return max(m) if float('-inf') in m else m[2]
        