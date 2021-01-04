#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) -1
        j = len(num2) -1
        result =""
        carry = 0
        while carry > 0 or i >=0 or j >= 0:
            if i>=0:
                carry += int(num1[i])
            if j>=0:
                carry += int(num2[j])
            
            result = str(carry%10) + result
            carry //= 10
            i -=1
            j -=1
        
        return result
# @lc code=end

