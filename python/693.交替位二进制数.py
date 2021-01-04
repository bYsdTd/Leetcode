#
# @lc app=leetcode.cn id=693 lang=python3
#
# [693] 交替位二进制数
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # 右移一位然后再异或，结果就是1111的形式
        # 左移是不行的，因为左移右边会补0，
        a = n ^ (n>>1)
        return a & (a +1) == 0
# @lc code=end

