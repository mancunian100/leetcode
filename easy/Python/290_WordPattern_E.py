# 知乎方法，查找相同元素时，都会返回第一个该元素的坐标，所以其实可以用这个坐标来判断是否是相同元素，机智
class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = pattern
        t = str.split()
        return list(map(s.find, s)) == list(map(t.index, t))  
                
        