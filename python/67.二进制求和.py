#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a)-1
        j = len(b)-1
        carry = 0
        result = ""
        while carry > 0 or i >=0 or j >=0:
            if i>= 0 and a[i] == '1':
                carry += 1
            
            if j>=0 and b[j] == '1':
                carry += 1
            
            result = str(carry%2) + result
            carry //= 2
            i -= 1
            j -= 1
            
        return result
            
# @lc code=end

