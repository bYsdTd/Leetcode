#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        left = 1
        for i in range(1,n):
            left *= nums[i-1]
            result[i] = left
        right = 1
        for i in range(n-2,-1,-1):
            right *= nums[i+1]
            result[i] *= right
        return result
# @lc code=end

