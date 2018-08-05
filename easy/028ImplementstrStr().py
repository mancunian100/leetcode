class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 先循环查找与needle第一个字符匹配的字符，找到后再验证后面的切片是否一致
        ln = len(needle)
        lh = len(haystack)
        if ln == 0:
            return 0
        for i in range(lh-ln+1):
            if haystack[i:i+ln] == needle:
                return i
        return -1