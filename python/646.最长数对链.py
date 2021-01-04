#
# @lc app=leetcode.cn id=646 lang=python3
#
# [646] 最长数对链
#

# @lc code=start
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # dp[i]表示以pairs[i]为最后一个数对的最长的数对链
        pairs = sorted(pairs, key=lambda x: x[0])
        # print(pairs)
        n = len(pairs)
        dp = [1] * n
        for i in range(n):
            for j in range(0,i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i],dp[j]+1)
        # print(dp)
        return max(dp)
        
# @lc code=end

