#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 用一个0-n的所有数与整个数组异或运算
        result = 0
        n = len(nums)
        for i in range(n):
            result = result ^ i ^ nums[i]
        
        result ^= n
        return result
# @lc code=end

