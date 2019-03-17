class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 借鉴cnn中对图像边界采取填充0的方法
        # 对值为1的元素，加4，并减去周围的值也为1的数量
        result = 0
        h, w = len(grid)+2, len(grid[0])+2
        grid.insert(0, [0]*w)
        grid.append([0]*w)
        for i in range(1, h-1):
            grid[i].insert(0, 0)
            grid[i].append(0)
        for i in range(1, h-1):
            for j in range(1, w-1):
                if grid[i][j]:
                    result += 4 * grid[i][j] - grid[i-1][j] - grid[i+1][j] - grid[i][j-1] - grid[i][j+1]
        return result