#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # backtracking函数,从当前的begin开始,end 为begin到n的子串里找是否是回文
        # 如果是，就从end+1继续递归backtracking
        n = len(s)
        result = []
        curres = []

        def ispa(begin:int, end:int) ->bool:
            nonlocal s
            while begin < end:
                if s[begin] != s[end]:
                    return False
                begin += 1
                end -= 1
            return True

        def backtracking(begin:int):
            nonlocal s
            if begin == n:
                result.append(curres.copy())
                return
                
            for e in range(begin, n):
                if ispa(begin, e):
                    curres.append(s[begin:e+1])
                    backtracking(e+1)
                    curres.pop()

            return
        
        backtracking(0)
        return result
# @lc code=end

