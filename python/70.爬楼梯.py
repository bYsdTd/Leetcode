#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
            
        cur = 0
        pre1 = 1
        pre2 = 2
        for _ in range(3,n+1):
            cur = pre1 + pre2
            pre1 = pre2
            pre2 = cur
        
        return cur
# @lc code=end

