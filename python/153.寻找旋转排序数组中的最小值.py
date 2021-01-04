#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 本质上是找到一个值比后面的值小的那个临界点
        # 正常都是这个临界点前面的值要比后面的值要大
        # 所以如果m比h的值大的话，如果临界点在右边，应该修改l
        # 如果m比h值小的话，临界点在左边

        # l = 0
        # n = len(nums)
        # h = n-1
        # while h-l > 1:
        #     m = l + int((h-l)/2)
        #     if nums[m] > nums[h]:
        #         l = m
        #     elif nums[m] < nums[h]:
        #         h = m
        
        # return nums[h] if nums[h] < nums[l] else nums[l]

        #-------------优化下方案-----------------------
        # 如果m比h大的话，临界点在右边，l=m+1，m肯定不是结果
        # 如果m比h小的话，临界点在左边，m也有可能是结果，h=m
        # 最后是相等的时候退出循环了
        # m>h，l=h=m+1，l 就是目标值 (7,0)这样的情况
        # m<h, 1=h=m,   同样l就是目标值(1, 2)这样的情况

        l = 0
        n = len(nums)
        h = n-1

        while l<h:
            m = l + int((h-l)/2)
            if nums[m] >= nums[h]:
                l=m+1
            else:
                h=m

        return nums[l]
        
# @lc code=end

