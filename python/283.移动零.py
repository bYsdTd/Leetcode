#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        cur = 0
        p = 0
        while cur < n:
            if nums[cur] != 0:
                nums[cur], nums[p] = nums[p], nums[cur]
                p += 1
            cur += 1
        
        return
# @lc code=end

