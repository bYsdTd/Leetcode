#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x ^ y
        count = 0
        while diff>0:
            count = count + 1 if diff & 0x1 else count
            diff >>=1
        
        return count
        
# @lc code=end

