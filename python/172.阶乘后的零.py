#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 由于10可以分解成2*5
        # 本质就是求1到n里面5的出现个数，因为2的个数肯定比5多
        # 5,10,15,20,25,30,35,40,45,50.....
        c5 = 0
        while n > 0:
            n //= 5
            c5 += n
            
        return c5
# @lc code=end

