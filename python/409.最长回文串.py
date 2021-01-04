#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        mp = set()
        l = 0
        for c in s:
            if c in mp:
                mp.remove(c)
                l += 2
            else:
                mp.add(c)
        
        l += 1 if len(mp) > 0 else 0

        return l

# @lc code=end

