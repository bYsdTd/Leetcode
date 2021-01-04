#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 先对candidate 排好序，这样相同的元素，如果以前面的作为begin已经找到了所有的组合，那么后面也就不用找了
        # 前面的candidate需要标记下访问的状态，当进入他开始的时候，标记为1，如果已经从他出来了，就要标记成0

        n = len(candidates)
        result = []
        curres = []
        lookup = [0] * n
        def backtracking(begin:int):
            nonlocal target
            # print("backtracking", begin, target)
            if target == 0:
                result.append(curres.copy())
                return

            for i in range(begin, n):
                if i > 0 and candidates[i] == candidates[i-1] and not lookup[i-1]:
                    continue
                
                if candidates[i] <= target:
                    lookup[i] = 1
                    curres.append(candidates[i])
                    target -= candidates[i]
                    backtracking(i+1)
                    lookup[i] = 0
                    target += candidates[i]
                    curres.pop()
                
                # lookup[i] = 1
            return
        
        candidates.sort()

        backtracking(0)
        return result
# @lc code=end

