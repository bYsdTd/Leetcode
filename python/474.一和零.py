#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#

# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for s in strs:
            cost0 = 0
            cost1 = 0
            for c in s:
                if c == '0':
                    cost0 +=1
                else:
                    cost1 +=1
            
            for i in range(m,cost0-1,-1):
                for j in range(n, cost1-1,-1):
                    dp[i][j] = max(dp[i][j], dp[i-cost0][j-cost1]+1)
        # print(dp)
        return dp[m][n]
# @lc code=end

