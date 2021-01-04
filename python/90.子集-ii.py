#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        curres = []
        lookup = [0] * n
        def backtracking(begin:int, k:int):
            nonlocal lookup
            if len(curres) == k:
                result.append(curres.copy())
                return
            
            for i in range(begin, n):
                if i > 0 and nums[i] == nums[i-1] and lookup[i-1] == 0:
                    continue
                curres.append(nums[i])
                lookup[i] = 1 # 入栈
                backtracking(i+1, k)
                lookup[i] = 0 # 出栈
                curres.pop()

            return
        
        nums.sort()
        for i in range(n+1):
            backtracking(0, i)
        return result
# @lc code=end

