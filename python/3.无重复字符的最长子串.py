#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.lengthOfLongestSubstringSlideWindow(s)

    def lengthOfLongestSubstringTwoPointer(self, s: str) -> int:
        maxLength=0
        curStart=0
        curEnd=0
        cm={}

        while curEnd < len(s) :
            if s[curEnd] in cm and cm[s[curEnd]] >= curStart:
                maxLength = max(curEnd-curStart, maxLength)
                curStart = cm[s[curEnd]]+1    
            else:
                maxLength = max(curEnd-curStart+1, maxLength)

            cm[s[curEnd]]=curEnd

            curEnd+=1
        
        return maxLength

    def lengthOfLongestSubstringSlideWindow(self, s: str) -> int:
        maxl = 0
        lookup = set()
        right = -1
        n = len(s)
        for i in range(n):
            if i != 0:
                lookup.remove(s[i-1])
            while right + 1 < n and s[right+1] not in lookup:
                lookup.add(s[right+1])
                right += 1
                maxl = max(maxl,right-i+1)
        
        return maxl

# @lc code=end

