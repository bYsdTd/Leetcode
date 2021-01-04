#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 统计字符出现的次数是否完全相同
        if len(s) != len(t):
            return False
            
        count = [0] * 26
        for c in s:
            count[ord(c)-ord('a')] +=1
        
        for c in t:
            count[ord(c)-ord('a')] -=1

        for c in count:
            if c!=0:
                return False

        return True
# @lc code=end

