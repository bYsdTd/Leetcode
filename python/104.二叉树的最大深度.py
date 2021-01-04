#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        # 递归求解，如果当前节点空，就返回0
        # 不空，就返回，左子树和右子树的最大深度 + 1
        
        if root == None:
            return 0
        
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)

        return max(l, r) + 1

# @lc code=end

