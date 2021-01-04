#
# @lc app=leetcode.cn id=413 lang=python3
#
# [413] 等差数列划分
#

# @lc code=start
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        # 等差数列的子区间个数
        n = len(A)
        dp = [0] * n
        for i in range(2,n):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                dp[i] = dp[i-1]+1
        count = 0
        for i in range(n):
            count += dp[i]
        return count
# @lc code=end

