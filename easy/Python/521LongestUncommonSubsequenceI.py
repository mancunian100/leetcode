class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # 根据首字母是否大写一共分为3种情况，是大写有2种
        l = len(word)
        if l < 2:
            return True
        word = [ord(i) for i in word]
        if word[0] in range(65, 91):
            temp = word[1] in range(65, 91)
            for i in word[1:]:
                if (i in range(65, 91)) != temp:
                    return False
        elif word[0] in range(97, 123):
            for i in word[1:]:
                if i in range(65, 91):
                    return False
        return True