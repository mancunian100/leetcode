class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        result = 0
        ng = ns = 0
        lg, ls = len(g), len(s)
        while ng < lg and ns < ls:
            if ns < ls and g[ng] <= s[ns]:
                result += 1
                ng += 1
                ns += 1
            else:
                ns += 1
        return result



g = [10, 9, 8, 7]
s = [5, 6, 7, 8]
print(Solution().findContentChildren(g, s))