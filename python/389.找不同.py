#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
            # countSet = {}
            # for c in s:
            #     if c in countSet:
            #         countSet[c]+=1
            #     else:
            #         countSet[c]=1
        
            # for c1 in t:
            #     if c1 in countSet:
            #         countSet[c1]-=1
            #         if countSet[c1] < 0:
            #             return c1
            #     else:
            #         return c1
        for c in t:
            if t.count(c)>s.count(c):
                return c
# @lc code=end

