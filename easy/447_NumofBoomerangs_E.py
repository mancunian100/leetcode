class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # 对于每一个点i，有k个点距离它相同的话，那么就有k*(k-1)个boomerangs
        re = 0
        for i in points:
            idist = {}
            for j in points:
                dx = i[0] - j[0]
                dy = i[1] - j[1]
                idist[dx*dx + dy*dy] = 1 + idist.get(dx*dx + dy*dy, 0)
                
            for k in idist:
                re += idist[k] * (idist[k] - 1)
                
        return re
                