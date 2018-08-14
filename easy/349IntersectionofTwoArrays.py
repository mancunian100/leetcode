class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 直接两层搜索，时间复杂度O(n^2)
        result = []
        for i in nums1:
            if i in nums2 and i not in result:
                result.append(i)
        return result

        # 使用dict，时间复杂度O(n)
        result = []
        dct = {}
        for i in nums1:
            if i not in dct.keys():
                dct[i] = 1
        for i in nums2:
            if i in dct.keys() and dct[i] == 1:
                result.append(i)
                dct[i] = 0
        return result