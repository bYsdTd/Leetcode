#
# @lc app=leetcode.cn id=376 lang=python3
#
# [376] 摆动序列
#

# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 用一个up和一个down来记录dp
        # 分别表示，以up和down为结尾的最后一次是上升的，还是下降的最大摆动序列的长度
        # 这样如果nums[i] > nums[i-1],就把前一个的down序列+1作为up的dp值
        # 小于同理，如果相等的话，up 和 down都应该跟前一个相同
        n = len(nums)
        if n == 0:
            return 0
        down = [1] * n
        up = [1] * n
        for i in range(1,n):
            if nums[i] - nums[i-1] > 0:
                up[i] = down[i-1]+1
                down[i] = down[i-1]
            elif nums[i] - nums[i-1] < 0:
                down[i] = up[i-1]+1
                up[i] = up[i-1]
            else:
                up[i] = up[i-1]
                down[i] = down[i-1]

        return max(max(up),max(down))


    def wiggleMaxLength1(self, nums: List[int]) -> int:
        # dp[i]表示以nums[i]结尾的最长的摆动序列
        # 考虑元素i与j[0,i)区间上进行比较,判断能否根据整个新增加的元素i，构成新的摆动序列，
        # 如果可以的话，就是dp[j]+1，最终的dp[i]应该是这些j中的最大值
        n = len(nums)
        if n == 0:
            return 0

        dp = [1] * n
        for i in range(n):
            for j in range(0,i):
                if (j == 0 and nums[i]-nums[j] != 0) or (nums[i] - nums[j]) * (nums[j]-nums[j-1]) < 0:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)
# @lc code=end

