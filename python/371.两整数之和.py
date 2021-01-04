#
# @lc app=leetcode.cn id=371 lang=python3
#
# [371] 两整数之和
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 考虑位运算的4种情况，00 10 01 11
        # 异或运算就是不进位的加法
        # 与运算可以把进位的位置找出来，左移1位就是进位
        # 递归求解，上面不进位和进位的结果的和
        # 但是由于python的整型数不是32位的，所以移位操作有问题
        # a = -1
        # a &= 0xffffffff
        # b = 1
        # print(bin(a), bin(b), bin(a^b), bin((a&b)<<1))
        # a,b = a^b,(a&b)<<1
        # print(bin(a), bin(b), bin(a^b), bin((a&b)<<1))
        a &= 0xffffffff
        b &= 0xffffffff
        # print(bin(a), bin(b))
        if b == 0:
            if a & 0x80000000:
                # print(bin(a), bin(a-1), bin()
                return -((~(a-1))&0x7fffffff)
            else:
                return a
        else:
            return self.getSum(a^b, (a&b)<<1)        
# @lc code=end

