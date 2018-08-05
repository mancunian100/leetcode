class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 不断对第一个str一个一个取字符，对比其他的prefix，直到与其他的不同，或者第一个字符串取完了
        result = ''
        l = len(strs)
        if l == 0:
            return ''
        if l == 1:
            return strs[0]
        l0 = len(strs[0])
        lr = 1
        while lr <= l0:
            for i in range(l):
                if strs[0][:lr] != strs[i][:lr]:
                    return strs[0][:lr-1]
            lr += 1
        return strs[0]