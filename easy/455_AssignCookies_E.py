class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # 排序后，每个cookie从小到大试娃，满足就给
        g.sort()
        s.sort()
        p1 = p2 = 0
        count = 0
        while p2 < len(s) and p1 < len(g):
            if s[p2] >= g[p1]:
                count += 1
                p1 += 1
                p2 += 1
            else:
                p2 += 1
                
        return count
        
        