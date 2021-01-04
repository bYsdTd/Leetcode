#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        # 准备一个hashmap
        # 遍历s，如果字符在mp中存在，并且mp[c]!=t[i] return false
        # 如果mp中不存在，就加入
        # 如果循环结束，就返回True
        mp = {}
        l = len(s)
        for i in range(l):
            if s[i] in mp and mp[s[i]] != t[i]:
                return False
            elif s[i] not in mp:
                mp[s[i]] = t[i]

        mp.clear()
        for i in range(l):
            if t[i] in mp and mp[t[i]] != s[i]:
                return False
            elif t[i] not in mp:
                mp[t[i]] = s[i]

        return True


        
# @lc code=end

