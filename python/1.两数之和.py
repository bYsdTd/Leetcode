#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=[]
        handled={}
        for i in range(0,len(nums)):
            remain = target - nums[i]
            if remain in handled:
                return [handled[remain], i]
            else:
                handled[nums[i]] = i

        return result

# @lc code=end

