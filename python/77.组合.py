#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 由于一直往后找，其实不需要lookup
        result = []
        # lookup = [0] * n
        curres = []
        
        def dfs(begin:int):
            if len(curres) == k:
                result.append(curres.copy())
                return

            for i in range(begin, n):
                # if lookup[i]:
                #     continue
                # lookup[i] = 1
                curres.append(i+1)
                dfs(i+1)
                # lookup[i] = 0
                curres.pop()


            return
        
        dfs(0)
        
        return result
        
# @lc code=end

