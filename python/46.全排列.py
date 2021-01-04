#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        lookup = [0] * n
        curres = []
        def dfs(i:int):
            lookup[i] = 1
            curres.append(nums[i])
            if len(curres) == n:
                result.append(curres.copy())
                lookup[i] = 0
                curres.pop()
                return

            for j in range(n):
                if lookup[j]:
                    continue
                dfs(j)
            curres.pop()
            lookup[i] = 0
            
            return

        for i in range(n):
            dfs(i)
        
        return result
# @lc code=end

