class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        maxCount = 0
        x = ''
        
        if s == '':
            return 0
        
        for i in s:
            if i not in x:
                x += i
                count += 1
            else:
                index = x.rfind(i)
                x = x[index+1:]+i
                count = len(x)
            if maxCount < count:
                maxCount = count
                rx = x
        return maxCount