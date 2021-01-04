#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lookup = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.cur = ""
        n = len(digits)
        result = []
        offset = ord('2')
        def dfs(digits:str, begin:int):
            if begin == n:
                result.append(self.cur)
                return
            index = ord(digits[begin]) - offset
            for char in lookup[index]:
                self.cur += char
                dfs(digits, begin+1)
                self.cur = self.cur[:begin]
            return
        if n == 0:
            return result
        dfs(digits, 0)
        return result
# @lc code=end

