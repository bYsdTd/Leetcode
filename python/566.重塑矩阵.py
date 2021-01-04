#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

# @lc code=start
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        oldR = len(nums)
        oldC = len(nums[0])
        if oldR * oldC != r * c:
            return nums

        newNums = [[0]*c for _ in range(r)]
        
        i = 0
        for row in range(r):
            for col in range(c):
                rowOld = int(i / oldC)
                colOld = i % oldC
                newNums[row][col] = nums[rowOld][colOld]
                i += 1
        
        return newNums
        
# @lc code=end

