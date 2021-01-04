#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:

        # 平方根一定在0-x之间
        # 这里终止条件是l<=h,
        # 最终运算之后因为h<l的
        # 所以应该返回h
        
        l = 0
        h = x
        while l <= h:
            m = l + int((h-l)/2)
            m2 = m*m
            if m2 == x:
                return m
            elif m2 < x:
                l = m+1
            else:
                h = m-1
        
        return h
# @lc code=end

