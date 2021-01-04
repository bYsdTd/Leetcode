#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        for _ in range(m):
            for j in range(1,n+1):
                dp[j] = dp[j]+dp[j-1]
        return dp[n]
# @lc code=end

