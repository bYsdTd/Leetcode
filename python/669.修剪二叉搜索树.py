#
# @lc app=leetcode.cn id=669 lang=python3
#
# [669] 修剪二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:

        def dfs(r:TreeNode) -> TreeNode:
            if not r:
                return None
            
            if r.val < low:
                r = dfs(r.right)
            elif r.val > high:
                r = dfs(r.left)
            else:
                r.left = dfs(r.left)
                r.right = dfs(r.right)

            return r
        
        return dfs(root)
        
# @lc code=end

