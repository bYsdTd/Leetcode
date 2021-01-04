#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第K小的元素
#

# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        low = matrix[0][0]
        high = matrix[n-1][n-1]
        
        # 这里为什么是小于，而不包含==
        # 除了第一次的low和high，后面的low和high已经都不能保证是矩阵中的值了
        # 由于我们的判断个数的条件是小于等于mid，所以最终当mid值不断缩小的时候
        # 当个数==k的是时候，mid值一定是等于k个元素里的最大值
        
        while low < high:
            mid = low + int((high-low)/2)
            num = 0
            row = n-1
            col = 0
            while row >=0 and col < n:
                if matrix[row][col] <= mid:
                    col += 1
                    num = num + row + 1
                else:
                    row -= 1
            
            # 左边的小于等于mid的个数比目标个数少,说明中间值小了，把中间值+1
            if num < k:
                low = mid+1
            # num == k的时候，说明当前的个数已经满足了，但是当前的中间值mid并不能确定就是等于low部分的最大值
            # 也有可能是比mid要小，所以这个时候的high应该设置成mid
            # num > k的时候也是同理
            elif num >= k:
                high = mid
        
        return low  

# @lc code=end

