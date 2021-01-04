#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#

# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        curMax = math.ceil(pow(c, 0.5))
        curMin = 0
        while curMin != curMax:
            s = curMin*curMin + curMax*curMax
            if s == c:
                return True
            elif s > c:
                curMax -= 1
            elif s < c:
                curMin +=1
        
        return c == curMin*curMin + curMax*curMax

# @lc code=end

