#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp[i]是以i结束的最长上升子序列的元素个数
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        # print(dp)
        return max(dp)
# @lc code=end

