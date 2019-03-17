class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 用一个长度为3的数组保存最大的3个元素，最后判断一下条件
        if not nums:
            return 0
        t = [float('-inf')] * 3
        for i in nums:
            for j in range(3):
                if i == t[j]:
                    break
                elif i > t[j]:
                    t.insert(j, i)
                    t.pop()
                    break
        if t[-1] != float('-inf'):
            return t[-1]
        else:
            return t[0]