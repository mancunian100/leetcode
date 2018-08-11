class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # 两层循环，注意首尾的1要手动添加，注意向上一层索引时的序号
        if numRows == 0:
            return []
        result = []
        row = 1
        while row <= numRows:
            s = []
            for i in range(row):
                if i == 0 or i == row-1:
                    s.append(1)
                else:
                    s.append(result[row-2][i-1] + result[row-2][i])
            result.append(s)
            row += 1
        return result

print(Solution().generate(5))