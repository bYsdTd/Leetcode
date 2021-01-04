#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node:'TreeNode', p: 'TreeNode', q: 'TreeNode')-> 'TreeNode':
            if not node or p == node or q == node:
                return node
            
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)

            return left if not right else right if not left else node

        return dfs(root, p, q)
        
# @lc code=end

