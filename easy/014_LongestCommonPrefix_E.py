class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if strs == []:
            return ''
        
        result = ''
        count = 0
        for i in strs[0]:
            result += i
            count += 1
            for j in strs[1:]:
                if result != j[0:count]:
                    result = result[:-1]
                    return result
        return result