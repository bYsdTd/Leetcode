#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        flag = 1
        for _ in range(32):
            if flag == n:
                return True
            flag <<=2
        return False
# @lc code=end

