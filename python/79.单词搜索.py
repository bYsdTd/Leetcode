#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.find = False
        m = len(board)
        n = len(board[0])
        lookup = [[0]*n for i in range(m)]
        wordlen = len(word)
        self.curIndex = 0
        prin = False
        def dfs(row:int, col:int):
            # if prin:
            #     print("dfs", row, col, self.curIndex)
            if row < 0 or col < 0 or row >= m or col >= n or self.curIndex == wordlen:
                if self.curIndex == wordlen:
                    self.find = True
                return

            if board[row][col] == word[self.curIndex] and lookup[row][col]==0:
                lookup[row][col] = 1
                self.curIndex += 1
                dfs(row-1,col)
                if self.find: return
                dfs(row+1, col)
                if self.find: return
                dfs(row, col-1)
                if self.find: return
                dfs(row, col+1)
                if self.find: return
                self.curIndex -= 1
                lookup[row][col] = 0

            return
        for row in range(m):
            for col in range(n):
                if not self.find:
                    # if row == 1 and col ==3:
                    #     # print(lookup)
                    #     prin = True
                    dfs(row,col)
        
        return self.find

# @lc code=end

