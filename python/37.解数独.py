#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    # def solveSudoku(self, board: List[List[str]]) -> None:
        # 用hashmap记录行，列，还有3x3里面1-9的数字是否使用过
        # 从某个格子开始，行优先遍历，或者列优先遍历，找到'.'的格子开始尝试填入，
        # 填入后就把行，列，还有3x3都标记成已使用这个数字

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 每一个有'.'的位置，可以放的数字满足3个条件
        # 横，竖，3x3内都是满足不重复的
        # 当前位置依次放入数字1-9，如果有不满足，就尝试下一个数字,如果都不满足，就回溯到上一个
        # 如果当前满足，就把对应的位置修改为目标值
        dic = "123456789"

        def backtracking() -> bool:
            nonlocal board
            nonlocal rowNumUsed
            nonlocal colNumUsed
            nonlocal cubeNumUsed
            
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        # fill = False
                        # for i in range(9):
                        #     # fill = canfill(row, col, dic[i])

                        #     if fill:
                        #         board[row][col] = dic[i]
                        #         # print("set ", row, col, dic[i])
                        #         fill = backtracking()
                        #         if not fill:
                        #             # if row == 0 and col ==2:
                        #                 # print("clear ", row, col, board[row][col])
                        #             board[row][col] = '.'
                        #         else:
                        #             return True

                        # if not fill:
                        #     return False

                        fill = False
                        for i in range(9):
                            if rowNumUsed[row][i] or colNumUsed[col][i] or cubeNumUsed[toCubeIndex(row, col)][i]:
                                continue
                            
                            board[row][col] = dic[i]
                            rowNumUsed[row][i] = 1
                            colNumUsed[col][i] = 1
                            cubeNumUsed[toCubeIndex(row, col)][i] = 1
                            # print("set ", row, col, )
                            fill = backtracking()
                            if not fill:
                                rowNumUsed[row][i] = 0
                                colNumUsed[col][i] = 0
                                cubeNumUsed[toCubeIndex(row, col)][i] = 0
                                board[row][col] = '.'
                            else:
                                return True

                        if not fill:
                            return False

            return True
        
        # def canfill(row:int, col:int, target:str) -> bool:
        #     nonlocal board
        #     # row
        #     for i in range(9):
        #         if col != i and board[row][i] == target:
        #             return False
        #     # col
        #     for i in range(9):
        #         if row != i and board[i][col] == target:
        #             return False
        #     # 3x3
        #     rowstart = row//3 * 3
        #     colstart = col//3 * 3
        #     for i in range(rowstart, rowstart+3):
        #         for j in range(colstart, colstart+3):
        #             if i != row and j != col and board[i][j] == target:
        #                 return False
            
        #     return True
        
        def toCubeIndex(row:int, col:int) -> int:
            r = row//3
            c = col//3
            return r * 3 + c

        rowNumUsed = [[0]*9 for i in range(9)]
        colNumUsed = [[0]*9 for i in range(9)]
        cubeNumUsed = [[0]*9 for i in range(9)]

        # 初始化num使用情况
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                num = ord(board[row][col]) - ord('1')
                rowNumUsed[row][num] = 1
                colNumUsed[col][num] = 1
                cubeNumUsed[toCubeIndex(row, col)][num] = 1

        backtracking()
# @lc code=end

