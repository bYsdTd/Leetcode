#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 求出数组的总和，如果总和本身是偶数 sum/2作为背包的容量
        # 认为容量和价值是相同的，那么问题就转化成sum/2的能装的最大容量是否==sum/2
        s = sum(nums)
        if s % 2 ==1:
            return False
        W = sum(nums)//2
        dp = [False] * (W+1)
        # n = len(nums)

        # # 方案1
        # for i in range(n):
        #     for j in range(W,0,-1):
        #         # 由于dp[j]需要用到上一行的数值，如果正向遍历的话，有可能dp[j]前面的值就被修改了
        #         # 所以j逆向遍历，保证
        #         if j >= nums[i]:
        #             dp[j] = max(dp[j],dp[j-nums[i]] + nums[i])    
        #         # temp = dp[j-nums[i]] + nums[i] if j >= nums[i] else 0
        #         # dp[j] = max(dp[j],temp)
        #     # print(i, dp)

        # 还可以用另一种思路，考虑用dp来记录容量是j的背包是否当前的i能放满
        # 如果i-1那一行已经放满了，那么i这一行也能放满,否则的话就是看dp[j-nums[i]]的那一个容量的背包放满了没有
        # dp[i][j] = dp[i-1][j] or dp[j-nums[i]]
        # 简化空间后 dp[j] = dp[j] or dp[j-nums[i]]
        # 如果j的背包容量比nums[i]还小的时候，就延续上一行的结果了
        # 方案2
        dp[0]=True
        for num in nums:
            for j in range(W,num-1,-1):
                dp[j] = dp[j] or dp[j-num]

        # return dp[W] == W
        return dp[W]
# @lc code=end

