#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    
    def findLeft(self, nums:[int], target:int) -> int:
        l = 0
        n = len(nums)
        h = n

        while l < h:
            m = l + int((h-l)/2)

            print(l,m,h)
            if nums[m] >= target:
                h = m
            else:
                l = m+1
        
        return l


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 先用二分查找，找到目标值，如果目标值不存在直接返回
        # 以目标值向两边分别找到不等于目标值的位置返回
        
        # l = 0
        # n = len(nums)
        # h = n-1

        # ptarget = -1
        # while l<=h:
        #     m = l + int((h-l)/2)
        #     if nums[m] == target:
        #         ptarget=m
        #         break
        #     elif nums[m] > target:
        #         # 在左边，移动h
        #         h = m-1
        #     elif nums[m] < target:
        #         # 在右边，移动l
        #         l = m+1
        
        # if ptarget==-1:
        #     return[-1,-1]

        # pmax=ptarget+1
        # pmin=ptarget-1
        # while pmin>=0:
        #     if nums[pmin] == target:
        #         pmin-=1
        #     else:
        #         pmin+=1
        #         break
        # while pmax<n:
        #     if nums[pmax] == target:
        #         pmax +=1
        #     else:
        #         pmax -=1
        #         break
        
        # pmin = pmin if pmin>=0 else 0
        # pmax = pmax if pmax<n else n-1
        # return [pmin, pmax]
        
        # 方案2 先找目标值最左边的位置
        # 还是普通的二分查找，
        # m>=target h 移动，h=m
        # m<target, l移动, l=m+1
        # 但是有可能有重复的元素，当m==target的时候，左边也可能有，右边也可能有，但是由于我们是想找到最左边的
        # 所以要保留左边和当前值,  保留左边就是要移动h，所以这种情况合并到m>target 里面，同时h=m
        # h初始要=n
        # 判定条件是l<h 由于h=m的设定，所以最后两个元素的时候，m=l，所以h=m=l了，就不能终止了
        # 最后结束时候，两个元素，如果左边是目标值，这时候m==target，所以h=m=l
        # 如果右边是目标值，m<target, l=m+1=h,不管怎么结束，多是l和h指向了同一个位置，都是目标值

        pmin = self.findLeft(nums, target)
        pmax = self.findLeft(nums, target+1)-1

        if pmin == len(nums) or nums[pmin] != target:
            return [-1,-1]
        else:
            return [pmin, max(pmin,pmax)]



# @lc code=end

