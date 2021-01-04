#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # DFS
        # 从每一个节点开始进行DFS，找其中最大的

        # 这里有个优化的巧妙的方法，但是改变了原始数据，就是把计算过的地方改成0了
        # 不改变原始数据的话，就需要用一个hashmap记录

        maxArea = 0
        maxRow = len(grid)
        maxCol = len(grid[0])
        self.offset = [[-1,0], [0,1], [1,0], [0,-1]]

        # self.visited = set()

        for row in range(maxRow):
            for col in range(maxCol):
                # index = row*maxCol+col
                # if index in self.visited:
                #     continue        
                maxArea = max(maxArea, self.DFSArea([row, col], grid, maxRow, maxCol))

        return maxArea

    def DFSArea(self, start:List[int], grid:List[List[int]], maxRow:int, maxCol:int) -> int:
        # 从节点开始向周围找，如果是1的话就继续向下找，
        # 如果是0或者超出边界了就返回,如果已经处理过了，就不处理
        # print("DFS", start)

        
        # index = start[0]*maxCol + start[1]
        

        if start[0] < 0 or start[0] >= maxRow or start[1] < 0 or start[1] >= maxCol or grid[start[0]][start[1]] == 0:
            return 0

        grid[start[0]][start[1]] = 0
        # if grid[start[0]][start[1]]:
            
            # if index in self.visited:
            #     return 0

            # self.visited.add(index)
        area = 1
        for o in self.offset:
            row = start[0]+o[0]
            col = start[1]+o[1]
            area += self.DFSArea([row, col], grid, maxRow, maxCol)
        
        return area

# @lc code=end

