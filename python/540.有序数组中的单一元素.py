#
# @lc app=leetcode.cn id=540 lang=python3
#
# [540] 有序数组中的单一元素
#

# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # 先找到m，然后分m是奇数还是偶数计算
        # 如果是奇数，并且与后面的相等，或者是偶数与前面的相等，这时候表示single在前面
        # 如果是奇数，并且与前面的相等，或者是偶数与后面的相等，这时候表示single在后面
        # 如果与前后都不相等，就找到了

        # 上面如果在前面的话，就把h设置成m+1(奇数)，或者设置成m(偶数)
        # 如果在后面的话，就把l设置成m-1(奇数)，或者设置成m（偶数）

        # l = 0
        # n = len(nums)
        # h = n-1
        # if n == 1:
        #     return nums[0]

        # while l < n:
        #     m = l + int((h-l)/2)

        #     if h - l == 2:
        #         return nums[l] if nums[m] == nums[h] else nums[h]

        #     if nums[m] != nums[m+1] and nums[m] != nums[m-1]:
        #         return nums[m]

        #     if (m % 2 == 1 and nums[m] == nums[m+1]):
        #         h = m + 1
        #     elif (m % 2 == 0 and nums[m] == nums[m-1]):
        #         h = m
        #     elif (m % 2 == 1 and nums[m] == nums[m-1]):
        #         l = m - 1
        #     elif (m % 2 == 0 and nums[m] == nums[m+1]):
        #         l = m
        
        # return 0


        # --------------------方案优化---------------
        # 可以把m都优化到偶数位置，这样只需要比较他后面的那个就可以了
        # 这样如果m与后面的值相等，就说明single在后面,l = m+2，这时候可能是后面的那个就是single，如果只剩下3个的时候，l就指向后面那个了
        # 如果m与后面值不相等，说明single在前面,h = m，可能前一个就是single，如果只有三个的时候，l就是结果
        # 
        l = 0
        n = len(nums)
        h = n-1

        while l < h:
            m = l + int((h-l)/2)
            if m % 2 == 1:
                m -= 1
            
            if nums[m] == nums[m+1]:
                l = m +2
            else:
                h = m
        

        return nums[l]


# @lc code=end

