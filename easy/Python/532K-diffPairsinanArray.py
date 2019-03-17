class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 注意审题，当k=0时只取一对相同的数字，而不是把相同的数字排列组合
        result = 0
        if k == 0:
            dct = {}
            for i in nums:
                if i not in dct.keys():
                    dct[i] = 1
                else:
                    dct[i] += 1
            for i in list(dct.values()):
                if i > 1:
                    result += 1
            return result
        elif k > 0:
            dct = {}
            for i in nums:
                if i not in dct.keys():
                    dct[i] = 1
                    result += int(i-k in dct.keys()) + int(i+k in dct.keys())
            return result
        else:
            return 0
            