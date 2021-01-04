#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        curres = []
        s = n
        def backtracking(begin:int):
            nonlocal s
            if s == 0 or len(curres) == k:
                if s == 0 and len(curres) == k:
                    result.append(curres.copy())
                return
            
            for i in range(begin,10):
                if i > s:
                    break
                curres.append(i)
                s -= i
                backtracking(i+1)
                curres.pop()
                s += i

            return
        
        backtracking(1)
        return result
# @lc code=end

