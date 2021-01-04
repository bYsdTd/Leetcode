#
# @lc app=leetcode.cn id=476 lang=python3
#
# [476] 数字的补数
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        result = 0
        flag = 0x80000000
        begin = False
        for _ in range(32):
            if flag & num > 0:
                begin = True
            else:
                if begin:
                    result |= flag

            flag >>=1
        # print(bin(result))
        return result
            
# @lc code=end

