#
# @lc app=leetcode.cn id=451 lang=python3
#
# [451] 根据字符出现频率排序
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        fmp = {}
        maxf = 0
        for c in s:
            fmp[c] = fmp[c] + 1 if c in fmp else 1
            maxf = max(maxf, fmp[c])

        buckets = []
        for _ in range(maxf+1):
            buckets.append("")
        
        for c,f in fmp.items():
            s = [c] * f
            buckets[f] += "".join(s)
        
        result = ""
        for i in range(maxf,0,-1):
            result += buckets[i]
        
        return result





# @lc code=end

