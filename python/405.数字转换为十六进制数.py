#
# @lc app=leetcode.cn id=405 lang=python3
#
# [405] 数字转换为十六进制数
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
        # 思路还是求余作为右边一位
        # 取整作为下次迭代的数值，
        # 只不过求余是按位运算的方式，除法是右移的方式
        # 之所以采用位运算的方式，是因为要考虑负数并且补码的形式
        # 以-1为例，ffffffff,一直右移，能保证每次运算都是f
        if num == 0:
            return "0"

        lookup = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        result = ""
        # count = 8
        num = num & 0xffffffff
        while num != 0:
            result = lookup[num&0b1111] + result
            num >>= 4
            # count -= 1
        
        return result
        
# @lc code=end

