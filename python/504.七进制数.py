#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        
        if num == 0:
            return "0"
            
        result = ""
        sign = ""
        if num < 0:
            num = -num
            sign = "-"

        while num > 0:
            remain = num % 7
            result = str(remain) + result
            num = int(num / 7)
        
        result = sign + result
        
        return result
        
# @lc code=end

