#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1 = float('-inf')
        max2 = float('-inf')
        max3 = float('-inf')
        min1 = float('inf')
        min2 = float('inf')
        for num in nums:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            else:
                if num > max2:
                    max3 = max2
                    max2 = num
                else:
                    if num > max3:
                        max3 = num
            
            if num < min1:
                min2 = min1
                min1 = num
            else:
                if num < min2:
                    min2 = num
        
        return max(min1*min2*max1, max1*max2*max3)
            
            

# @lc code=end

