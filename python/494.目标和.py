#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    def findTargetSumWays1(self, nums: List[int], S: int) -> int:
        # dfs
        # 每个位置都可以是正负两种情况，把nums的规模缩小，同时把两种情况不同的S值递归求解
        # 返回的值应该是两种情况的总和
        # su = sum(nums) 
        # W = su+S
        # if su < S:
        #     return 0
        # if W%2 == 1:
        #     return 0

        n = len(nums)
        def dfs(b:int,target:int) -> int:
            # print("dfs ", b, target)
            if b == n:
                return 1 if target == 0 else 0

            return dfs(b+1, target+nums[b]) + dfs(b+1,target-nums[b])

        return dfs(0, S)

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # 把分为正和负两个部分
        # p - n = s
        # p = s + n
        # 2p = s + sum
        # p = (s + sum)/2
        # 找到子序列和等于sum = (s+sum)/2的方法数
        su = sum(nums) 
        W = su+S
        if su < S:
            return 0
        if W%2 == 1:
            return 0
        W //=2
        dp = [0] * (W+1)
        dp[0] = 1
        for num in nums:
            for j in range(W,num-1,-1):
                dp[j] = dp[j] + dp[j-num]
        
        return dp[W]
        
# @lc code=end

