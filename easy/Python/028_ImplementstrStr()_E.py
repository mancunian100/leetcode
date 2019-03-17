class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle is '':
            return 0
        elif haystack is '':
            return -1
        else:
            ln = len(needle)
            lh = len(haystack)
            if ln > lh:
#                 print('>')
                return -1
            for i in range(0, lh-ln+1):
#                 print(haystack[i])
                if haystack[i] == needle[0]:
#                     print('f')
                    if haystack[i:i+ln] == needle:
                        return i
#             print('finished')
            return -1