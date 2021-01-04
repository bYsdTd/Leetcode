#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        lookup = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        while n > 0:
            result = lookup[(n-1)%26] + result
            n = (n-1)//26
        
        return result
# @lc code=end

