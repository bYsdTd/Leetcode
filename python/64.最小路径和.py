#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = [[0]*n for i in range(m)]

        dp = [float("inf")] * (n+1) #一维数组记录

        dp[1] = 0
        for row in range(m):
            for col in range(1, n+1):
                dp[col] = min(dp[col], dp[col-1]) + grid[row][col-1]
                # print(row, col, dp[col])
                # if row == 0 and col == 0:
                #     result[row][col] = grid[row][col]
                #     continue

                # up = float("inf")
                # left = float("inf")
                # if row != 0:
                #     up = result[row-1][col]
                
                # if col != 0:
                #     left = result[row][col-1]
                # result[row][col] = min(up, left) + grid[row][col]
        # print(dp)
        # return result[m-1][n-1]
        return dp[n]
                    

# @lc code=end

