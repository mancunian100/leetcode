class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 为了处理最后一个单词，额外写了一个循环外的判断，感觉很啰嗦
        result = ''
        temp = ''
        for i in s:
            if i == ' ':
                if temp != '':
                    l = len(temp)
                    for j in range(l):
                        result += temp[l-1-j]
                temp = ''
                result += ' '
            else:
                temp += i
        if temp:
            l = len(temp)
            for j in range(l):
                result += temp[l-1-j]
        return result