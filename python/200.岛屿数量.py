#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS的算法
        # 考虑计算每个元素为起点的岛屿
        # 计算岛屿的过程中都设置成0()，
        # 对row和col遍历，如果是岛屿的话就返回>0的数
        return self.numIslandsDFS(grid)

    def DFSIsIsland(self, grid: List[List[str]], row:int, col:int) -> int:
        if row < 0 or col < 0 or row >= self.maxRow or col >= self.maxCol or grid[row][col] == '0':
            return 0
        
        grid[row][col] = '0'
        area = 1

        for o in self.offset:
            area += self.DFSIsIsland(grid, row+o[0], col+o[1])

        return area

    def numIslandsDFS(self, grid: List[List[str]]) -> int:
        
        self.offset = [[-1,0], [0,1], [1,0], [0,-1]]
        self.maxRow = len(grid)
        self.maxCol = len(grid[0])

        count = 0
        for row in range(self.maxRow):
            for col in range(self.maxCol):
                if self.DFSIsIsland(grid,row, col) > 0:
                    count +=1

        return count
        
    

# @lc code=end

