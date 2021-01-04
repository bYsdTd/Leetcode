#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution:

        
    def solve(self, board: List[List[str]]) -> None:
        # self.dfsFill(board)
        self.dfsFillOpt(board)

    # 问题1，dfs的结果最后才知道，是否到达边缘，那么中间过程的节点保存在哪里
    # 问题2，标记完成的节点，需要row，col的坐标，用什么数据结构保存
    # 以上两个问题的优化方案是，逆向思维
    # 如果一个O与边缘的相连，那么它就不应该被填充
    # 所以从边缘开始DFS运算，把遍历到的O都标记成T
    # 这样最终的矩阵里，由于边缘相连的都标成T了，那么O就都是需要填充的
    # T都变回去O，就可以了

    def dfsFillOpt(self, board: List[List[str]]) -> None:
        
        self.m = len(board)
        if self.m==0:
            return
        self.n = len(board[0])

        for r in range(self.m):
            self.dfsOpt(board, r, 0)
            self.dfsOpt(board, r, self.n-1)

        for c in range(self.n):
            self.dfsOpt(board, 0, c)
            self.dfsOpt(board, self.m-1, c)

        for r in range(self.m):
            for c in range(self.n):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
        

    def dfsOpt(self, board: List[List[str]], r:int, c:int) -> None:
        if r < 0 or c < 0 or r >= self.m or c >= self.n or board[r][c] != 'O':
            return

        board[r][c] = 'T'
        self.dfsOpt(board, r+1, c)
        self.dfsOpt(board, r-1, c)
        self.dfsOpt(board, r, c+1)
        self.dfsOpt(board, r, c-1)

    def dfs(self, board: List[List[str]], c:tuple, visited:List[tuple]) -> bool:

        if c[0]<0 or c[0] >= self.m or c[1] < 0 or c[1] >= self.n:
            # 到达边缘
            return False
        
        if self.visited[c[0]][c[1]]:
            return True

        self.visited[c[0]][c[1]] = 1
        visited.append(c)
            
        if board[c[0]][c[1]] == 'O':
            result = True
            for o in self.offset:
                row = c[0]+o[0] 
                col = c[1]+o[1]

                # result 要放到后面，不然如果false的话，就不执行后面了
                result = self.dfs(board, (row, col), visited) and result

            return result
        else:
            return True

        return True

    def dfsFill(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 从O的节点开始，进行DFS，如果最终没有到达边缘，那么遍历过的节点都应该设置成X
        # DFS搜索到的O节点都加入visited
        self.visited = []
        self.m = len(board)
        if self.m==0:
            return

        self.n = len(board[0])

        for i in range(self.m):
            self.visited.append([0]*self.n)

        self.offset = [(-1,0), (1,0), (0,1), (0, -1)]

        for row in range(1,self.m-1):
            for col in range(1, self.n-1):
                c = (row, col)
                if not self.visited[row][col] and board[row][col] == 'O':
                    v = []
                    if self.dfs(board, c, v):
                        for p in v:
                            board[p[0]][p[1]] = 'X'

# @lc code=end

