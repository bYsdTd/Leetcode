#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    
    def isPerfectSquare(self, num: int) -> bool:
        # 通过等差数列
        s = 1
        while num>0:
            num -= s
            s += 2
        return num == 0
        
    def isPerfectSquare1(self, num: int) -> bool:
        l = 0
        h = num
        while l < h:
            mid = l + (h-l)//2
            mp = mid * mid
            if mp == num:
                return True
            elif mp < num:
                l = mid+1
            else:
                h = mid-1
            
        return l*l == num

    
# @lc code=end

