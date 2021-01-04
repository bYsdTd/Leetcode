#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:

        def dfsright(node: TreeNode, upRightTotal:int) -> int:
            if not node:
                return upRightTotal
            res = dfsright(node.right, upRightTotal)
            node.val += res
            return dfsright(node.left, node.val)

        dfsright(root, 0)
        return root
        
# @lc code=end

