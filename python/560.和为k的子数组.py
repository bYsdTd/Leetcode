#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: [int], k: int) -> int:
        # n=len(nums)
        # count=0
        # for start in range(0,n):
        #     curSum=0
        #     for end in range(start,n):
        #         curSum+=nums[end]
        #         if curSum==k:
        #             count+=1

        # return count 
        mp=collections.defaultdict(int)
        pre=0
        count=0
        mp[0]=1

        for num in nums:
            pre+=num
            if pre-k in mp:
                count+=mp[pre-k]
            
            mp[pre]+=1

        return count 
# @lc code=end

