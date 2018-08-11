class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]

        pre = [1,1]
        row = []
        if rowIndex > 1:
            for i in range(0, rowIndex-1):
                row.append(1)
                for j in range(0, len(pre)-1):
                    row.append(pre[j]+pre[j+1])
                row.append(1)
                
                pre = row
                row = []
        return pre
        