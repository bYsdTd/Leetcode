#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        marked = [1] * (n+1)
        for i in nums:
            marked[i] -= 1
        
        copy = -1
        lost = -1
        for i in range(1,n+1):
            if marked[i] == -1:
                copy = i
            elif marked[i] == 1:
                lost = i
            
            if copy >= 0 and lost >= 0:
                break
        
        return [copy, lost]
        
        
# @lc code=end

