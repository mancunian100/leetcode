class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]

        pre = [1,1]
        row = []
        result = [[1],[1,1]]
        if numRows > 2:
            for i in range(0, numRows-2):
                row.append(1)
                for j in range(0, len(pre)-1):
                    row.append(pre[j]+pre[j+1])
                row.append(1)
                
                result.append(row)
                pre = row
                row = []
        return result