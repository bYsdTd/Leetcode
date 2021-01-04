#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[j][k]表示前i个单词是否可以对j,k之间的单词完全覆盖
        # 考虑第i个单词取和不取的情况，如果dp[j]本来就可以覆盖就不用管，如果不能的话
        # 看s 是否在包含单词i，如果包含的话，
# @lc code=end

