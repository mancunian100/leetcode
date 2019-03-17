class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # 注意题意，set对象进行对比就需要两边都换成set
        key1 = set('qwertyuiop')
        key2 = set('asdfghjkl')
        key3 = set('zxcvbnm')
        result = []
        for word in words:
            temp = set(word.lower())
            if temp & key1 == temp:
                result.append(word)
            elif temp & key2 == temp:
                result.append(word)
            elif temp & key3 == temp:
                result.append(word)
        return result

a = ["Hello","Alaska","Dad","Peace"]

print(Solution().findWords(a))