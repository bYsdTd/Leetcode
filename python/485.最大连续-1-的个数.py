#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续1的个数
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        m = 0
        for i in nums:
            if i:
                count += 1
                m = max(m, count)
            else:
                count = 0
        
        return m
        
# @lc code=end

