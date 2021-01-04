#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 皇后的所在行，列，斜线只能有一个q
        # rowQueue = [0] * n # 第row行是否有queue
        # 其实行的记录是不需要的，因为每次都是以一行为遍历，这一行能放入q的话，就直接到下一行了
        # 这一行放不了也直接递归退回了
        
        colQueue = [0] * n # 第col列是否有queue
        ltQueue = [0] * (2*n-1) # 左上右下对角线
        rtQueue = [0] * (2*n-1)

        # result = [['.'] * n for i in range(n)]
        result = []
        curres = [['.']*n for i in range(n)]
        remainQ = n
        
        def toLtIndex(row:int, col:int) -> int:
            return (row - col + n - 1)
        
        def toRtIndex(row:int, col:int) -> int:
            return (row + col)

        # 从某一个row，col开始，
        # 找到一个可以放入Q的位置(行，列，斜线都没有q)
        # 修改行列，斜线记录，修改remainQ，修改当前curres
        # 继续下一行，(row+1,0)开始递归
        # 如果递归结果返回失败，就把上面的状态都修改回去

        def backtracking(row:int) ->bool:
            nonlocal remainQ
            if remainQ == 0:
                result.append([''.join(s) for s in curres])
                return True
            
            col = 0
            while col < n:
                if curres[row][col] !='Q' and not colQueue[col] and not ltQueue[toLtIndex(row,col)] and not rtQueue[toRtIndex(row, col)]:
                    curres[row][col] = 'Q'
                    remainQ -= 1
                    colQueue[col] = ltQueue[toLtIndex(row,col)] = rtQueue[toRtIndex(row, col)] = 1
                    backtracking(row+1)
                    colQueue[col] = ltQueue[toLtIndex(row,col)] = rtQueue[toRtIndex(row, col)] = 0
                    curres[row][col] = '.'
                    remainQ += 1
                col += 1
            return False
        
        backtracking(0)
        return result
# @lc code=end

