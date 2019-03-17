class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        t = 0
        for i in range(0,n):
            print(nums2[i])
            j = t
            while(j < m+n):
                if nums2[i] < nums1[j]:
                    nums1.insert(j, nums2[i])
                    nums1.pop(-1)
                    t = j 
                    break
                j += 1
                if j > m+i:
                    nums1[j-1] = nums2[i]
                    break
                print(j,nums1)

nums1 = [0]
m = 0
nums2 = [2]      
n = 1
Solution().merge(nums1,m,nums2,n)
print(nums1)

