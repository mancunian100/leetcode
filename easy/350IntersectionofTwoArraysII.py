class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 使用dct计数，时间复杂度O(n)
        dct = {}
        result = []
        for i in nums1:
            if i not in dct.keys():
                dct[i] = 1
            else:
                dct[i] += 1
        for i in nums2:
            if i in dct.keys() and dct[i] > 0:
                dct[i] -= 1
                result.append(i)
        return result