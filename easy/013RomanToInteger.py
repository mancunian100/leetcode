class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # define a dict to rank the Roman numerals
        # if the order of Roman numerals is not descending, then the previous one should be reduced
        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        l = len(s)
        result = 0
        for i in range(l-1):
            sig = 1
            if roman_dict[s[i]] < roman_dict[s[i+1]]:
                sig = -1
            result += sig * roman_dict[s[i]]
        result += roman_dict[s[-1]]
        return result

s = "MCMXCIV"
print(Solution().romanToInt(s))