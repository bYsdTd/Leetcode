#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 0 if s[0] == '0' else 1

        dp = [0] * (n+1)
        dp[0] = dp[1] = 1 if s[0] != '0' else 0
        #dp[1]表示下标0左边的编码
        for i in range(2,n+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            tmp = int(s[i-2:i])
            if tmp <= 26 and tmp>0 and s[i-2] != '0':
                dp[i] += dp[i-2]
        
        # print(dp)
        return dp[n]
# @lc code=end

