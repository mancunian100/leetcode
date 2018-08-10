class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rx = 0
        preii = 1000

        romanDict = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        for i in s:
            ii = romanDict[i]
            if preii < ii:
                rx -= 2*preii
                rx += ii
            else:
                rx += ii
            preii = ii
        return rx