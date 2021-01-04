#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[j] 考虑第i个硬币，表示前i个硬币，如果目标金额是j的情况下能取完的组合数
        # 如果第i个金币考虑取和不取两种，取的话就是dp[j-coin[i]],不取的话就是dp[j]
        # 总组合数就是dp[j-coin[i]] + dp[j]
        # 最后返回dp[amount]
        dp = [0]*(amount+1)
        dp[0]=1
        for coin in coins:
            for j in range(coin,amount+1):
                dp[j] = dp[j]+dp[j-coin]
        
        return dp[amount]
# @lc code=end

