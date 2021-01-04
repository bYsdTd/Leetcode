#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        result = []
        s = 0
        curres = []
        def dfs(begin:int):
            count = 0
            nonlocal s
            if begin >= n:
                return
            while s < target:
                curres.append(candidates[begin])
                s += candidates[begin]
                count += 1
            
            if s == target:
                result.append(curres.copy())

            while count > 0:
                s -= curres.pop()
                dfs(begin+1)
                count -= 1
            
            return
        
        dfs(0)
        return result
 # @lc code=end

