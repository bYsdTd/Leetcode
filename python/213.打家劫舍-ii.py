#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 由于环形设计，所以opt(n-1) n-1是下标
        # 就分为选和不选，选的话，其实就是求从[1:n]的opt()
        # 不选的话，就是求[0:n-1]的opt
        def opt(nums:List[int], begin:int, end:int) -> int:
            n = end-begin+1
            if n == 1:
                return nums[begin]
            pre1 = nums[begin]
            pre2 = max(pre1, nums[begin+1])
            cur = pre2
            for i in range(begin+2,end+1):
                cur = max(pre1+nums[i], pre2)
                pre1 = pre2
                pre2 = cur
            return cur
        
        n = len(nums)
        if n == 1:
            return nums[0]
        
        return max(opt(nums,0,n-2), opt(nums,1,n-1))

        
# @lc code=end

