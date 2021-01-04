#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
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
        
        def dfs(node:'TreeNode', minimum: 'TreeNode', maxmum: 'TreeNode') -> 'TreeNode':
            if node.val > maxmum.val:
                return dfs(node.left, minimum, maxmum)
            elif node.val < minimum.val:
                return dfs(node.right, minimum, maxmum)
            
            return node
        
        minnode = p if p.val <= q.val else q
        maxnode = p if p.val > q.val else q

        return dfs(root, minnode, maxnode)
# @lc code=end

