class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 递归，表示出第k-1到第k个的表达式，第一个即1
        # 关键是记录字符在变化之前所重复的次数，用计数器count记录次数，字符记号char记录进行重复的字符
        result = ''
        if n == 1:
            result = '1'
            return result
        else:
            count = 0
            char = ''
            s = self.countAndSay(n-1)
            for i in s:
                if char != i:
                    if char != '':
                        result += str(count) + char
                    char = i
                    count = 1
                else:
                    count += 1
            result += str(count) + char
            return result