#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        curres = []
        lookup = [0] * n
        # localset = [set() for i in range(n)]

        def dfs():
            curlen = len(curres)
            if curlen==n:
                result.append(curres.copy())
                return
            localset = set()
            for i in range(n):
                # print(i, curlen, lookup)
                if lookup[i] == 1 or nums[i] in localset:
                    continue

                localset.add(nums[i])
                curres.append(nums[i])
                lookup[i]=1
                dfs()
                lookup[i]=0
                curres.pop()

            # localset[curlen].clear()
            
        dfs()
        
        return result
# @lc code=end

