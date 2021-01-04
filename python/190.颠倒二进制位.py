#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        # n最低位赋值给结果，然后结果左移，n右移
        result = 0
        for _ in range(32):
           result <<= 1
           result |= n & 1
           n >>= 1
            
        return result 
        
# @lc code=end

