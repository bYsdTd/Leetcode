#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p1 = 0
        p2 = n-1
        i = 0

        while i <= p2:
            if nums[i] == 0:
                nums[p1], nums[i] = nums[i], nums[p1]
                p1 +=1
                i += 1
            elif nums[i] == 2:
                nums[p2], nums[i] = nums[i], nums[p2]
                p2 -=1
            else:
                i += 1



# @lc code=end

