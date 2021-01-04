#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        row = m-1
        col = 0
        while row >=0 and col < n:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                col += 1
            else:
                row -= 1
        
        return False
    #         
        # print("hello")
    #     self.maxrow = len(matrix)

    #     if self.maxrow == 0:
    #         return False
    #     self.maxcol = len(matrix[0])

    #     return self.searchMatrixDC(matrix, target, 0, 0, self.maxrow-1, self.maxcol-1)
    
    # def searchMatrixDC(self, matrix, target, top, left, bottom, right) -> bool:
    #     # print("searchMatrixDC", top, left, bottom, right)
    #     # middowr = top + int((bottom-top)/2)
    #     # middowc = left + int((right-left)/2)
    #     # print("searchMatrixDC", top, left, bottom, right, middowr, middowc)
    #     if top < 0 or left < 0 or bottom < 0 or right < 0 or bottom >= self.maxrow or right >= self.maxcol:
    #         return False

    #     if target == matrix[bottom][right]:
    #         return True
    #     elif target > matrix[bottom][right]:
    #         return False
    #     else:

    #         middowr = top + int((bottom-top)/2)
    #         middowc = left + int((right-left)/2)
    #         if self.searchMatrixDC(matrix, target, top, left, bottom-1, right-1):
    #             return True
    #         elif self.searchMatrixDC(matrix, target, top, right, bottom-1, right):
    #             return True
    #         else:
    #             return self.searchMatrixDC(matrix, target, bottom, left, bottom, right-1)
            
# @lc code=end

