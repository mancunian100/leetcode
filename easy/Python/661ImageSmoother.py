import copy

class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        # 对边界的处理值得学习记忆，用max和min来选择边界的值
        # 深复制copy.deepcopy()是python里唯一一种单独把列表中的列表进行独立复制的方法
        h, w = len(M), len(M[0])
        N = copy.deepcopy(M)
        for i in range(h):
            for j in range(w):
                m = range(max(0, i-1), min(h-1, i+1)+1)
                n = range(max(0, j-1), min(w-1, j+1)+1)
                N[i][j] = int(sum([M[x][y] for x in m for y in n])/(len(m)*len(n)))
        return N

M = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]

print(Solution().imageSmoother(M))