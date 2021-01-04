#
# @lc app=leetcode.cn id=462 lang=python3
#
# [462] 最少移动次数使数组元素相等 II
#

# @lc code=start
import random
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        return self.minMoves2Quick(nums)

    def minMoves2Quick(self, nums: List[int]) -> int:
        n = len(nums)
        def partition(numslist:List[int], low:int, high:int) ->int:
            cur = low
            temp = random.randint(low, high)
            numslist[temp], numslist[high] = numslist[high], numslist[temp]
            
            for i in range(low, high):
                if numslist[i] < numslist[high]:
                    numslist[i], numslist[cur] = numslist[cur], numslist[i]
                    cur += 1
            numslist[cur], numslist[high] = numslist[high], numslist[cur]
            return cur
        
        self.midIndex = 0
        def findKthSmall(numslist:List[int], low:int, high:int, k:int):
            if low == high:
                self.midIndex = low
                return

            # if low>high or low < 0 or high < 0 or low >= n or high >= n:
            #     return
            index = partition(numslist, low, high)
            if index == k:
                self.midIndex = index
                return
            elif index < k:
                findKthSmall(numslist, index+1,high,k)
            elif index > k:
                findKthSmall(numslist, low, index-1, k)

        s = 0
        findKthSmall(nums,0,n-1,n//2)
        for i in range(n):
            s += abs(nums[i]-nums[self.midIndex])

        return s

    def minMoves2Sort(self, nums: List[int]) -> int:
        # 直接排序
        nums.sort()
        s = 0
        n = len(nums)
        for i in range(n//2):
            s += nums[n-i-1] - nums[i]
        
        return s

    
            
# @lc code=end

