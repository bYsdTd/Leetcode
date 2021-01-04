#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)

        if abs(l-r) > 1: self.result = False

        return max(l, r)+1

    def isBalanced(self, root: TreeNode) -> bool:
        # 要找到是否是平衡的二叉树，其实本质是计算深度
        # 那么在计算最大深度的过程中，发现左子树和右子树的深度差超过1了，就标记结果为false

        self.result = True
        self.maxDepth(root)

        return self.result
# @lc code=end

