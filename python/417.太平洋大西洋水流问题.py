#
# @lc app=leetcode.cn id=417 lang=python3
#
# [417] 太平洋大西洋水流问题
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # 逆向思维
        # 先找能流到太平洋的所有节点，再找能流到大西洋的所有节点, BFS,DFS都可以
        # 最后遍历所有节点，如果在以上两个集合里都有，就添加到结果列表里

        self.m = len(matrix)
        if self.m == 0:
            return None
        self.n = len(matrix[0])

        self.reachedP = [[0]*self.n for _ in range(self.m)]
        self.reachedA = [[0]*self.n for _ in range(self.m)]
        self.visited = [[0]*self.n for _ in range(self.m)]
        self.result = []
        self.offset = [[-1,0],[1,0],[0,1],[0,-1]]
        self.visited = [[0]*self.n for _ in range(self.m)]
        for r in range(self.m):
            self.dfs(matrix, r, 0, self.reachedP)
        
        self.visited = [[0]*self.n for _ in range(self.m)]
        for r in range(self.m):
            self.dfs(matrix, r, self.n-1, self.reachedA)

        self.visited = [[0]*self.n for _ in range(self.m)]
        for c in range(self.n):
            self.dfs(matrix, 0, c, self.reachedP)
        
        self.visited = [[0]*self.n for _ in range(self.m)]
        for c in range(self.n):
            self.dfs(matrix, self.m-1, c, self.reachedA)

        
        for r in range(self.m):
            for c in range(self.n):
                if self.reachedA[r][c] and self.reachedP[r][c]:
                    self.result.append([r,c])
        
        # print(self.reachedA, self.reachedP)

        return self.result

    # DFS有两种判定，一种是当前节点直接判定
    # 一种是在当前节点周围的节点是否进行递归的时候判定
    # 由于这个题的判定依赖周围的节点，所以要放在周围判定里面
    # 如果节点自己的数据就可以判定，就可以直接判定
    def dfs(self, matrix:List[List[int]], r:int, c:int, reached: List[List[int]]) -> None:
            # 这里进来的一定都是范围内的节点
            reached[r][c] = 1

            for o in self.offset:
                newRow = r + o[0]
                newCol = c + o[1]
                if newRow < 0 or newRow >= self.m or newCol < 0 \
                    or newCol >= self.n \
                    or self.visited[newRow][newCol] \
                    or reached[newRow][newCol] \
                    or matrix[newRow][newCol] < matrix[r][c]:
                    continue

                self.dfs(matrix, newRow, newCol, reached)


            
# @lc code=end

