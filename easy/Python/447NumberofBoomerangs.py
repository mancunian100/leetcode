class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # 每个点若有k个点与其相同距离，则可以组成k(k-1)满足条件
        result = 0
        for i in points:
            dis = {}
            for j in points:
                l1 = j[0] - i[0]
                l2 = j[1] - i[1]
                dis[l1**2 + l2**2] = dis.get(l1**2 + l2**2, 0) + 1
            for k in dis:
                result += (dis[k])*(dis[k]-1)
        return result