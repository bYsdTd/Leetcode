#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # flag = 1
        # for _ in range(32):
        #     if flag == n:
        #         return True
        #     flag <<=1
        # return False

        # 用n 和 n-1 1000 & 0111这样来判断
        return n > 0 and n &(n-1) == 0

# @lc code=end

