#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        handled=set()
        for num in nums:
            handled.add(num)

        return len(handled)<len(nums)
# @lc code=end

