#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#

# @lc code=start
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        numForKeys = {}
        for num in nums:
            if num in numForKeys:
                numForKeys[num]+=1
            else:
                numForKeys[num]=1

        
        longest = 0
        for key,count in numForKeys.items():
            if key+1 in numForKeys:
                longest = max(count+numForKeys[key+1], longest)

        return longest 
# @lc code=end

