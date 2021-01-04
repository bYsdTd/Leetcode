#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 0:
            return 0
        pre1 = nums[0]
        pre2 = max(nums[0], nums[1])
        if n == 2:
            return pre2
        cur = 0
        for i in range(2,n):
            cur = max(pre1 + nums[i], pre2)
            pre1 = pre2
            pre2 = cur
        return cur
# @lc code=end

