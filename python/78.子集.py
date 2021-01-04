#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        curres = []

        def backtracking(begin:int, k:int):
            if len(curres) == k:
                result.append(curres.copy())
                return

            for i in range(begin, n):
                curres.append(nums[i])
                backtracking(i+1, k)
                curres.pop()

            return
        
        for i in range(n+1):
            backtracking(0, i)
        
        return result
# @lc code=end

