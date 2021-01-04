#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0
        self.l = len(s)
        for i in range(self.l):
            self.extend(s, i, i)
            self.extend(s, i, i+1)
        
        return self.count

    def extend(self, s:str, start:int, end:int) -> None:
        while start>=0 and end <self.l and s[start] == s[end]:
            start -= 1
            end +=1
            self.count +=1

# @lc code=end

