class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # 在nums1中插入nums2满足顺序的数，每一次插入都减去最后的一个零
        # 最后还有nums2剩下的就将其整个赋给nums1末尾
        index1, index2 = 0, 0
        while index1 < m and index2 < n:
            if nums1[index1] > nums2[index2]:
                nums1.insert(index1, nums2[index2])
                nums1.pop()
                index1 += 1
                m += 1
                index2 += 1
            else:
                index1 += 1
        if index2 < n:
            nums1[index2-n:] = nums2[index2:]