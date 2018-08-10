class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # 把每一层while循环的结果存在result中，每次从上一个result进行计算
        result = []
        if rowIndex == 0:
            result = [1]
        r = 0
        while r <= rowIndex:
            s = []
            for i in range(r+1):
                if i == 0 or i == r:
                    s.append(1)
                else:
                    s.append(result[i-1] + result[i])
            result = s
            r += 1
        return result