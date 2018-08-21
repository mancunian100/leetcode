class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 这种直接方法太啰嗦了，以后要写一种简洁的
        na, nl = 0, 0
        for i in s:
            if i == 'A':
                na += 1
                nl = 0
            elif i == 'L':
                nl += 1
            elif i == 'P':
                nl = 0
            if na > 1:
                return False
            if nl > 2:
                return False
        return True