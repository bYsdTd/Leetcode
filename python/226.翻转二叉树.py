#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 翻转的意思是左右子树调换吗?
        # 还是递归的思想，就是交换左右两个节点的位置
        # 如果当前节点空，就什么都不做
        # 不空的话，就分别递归调用左叶子和右叶子节点
        # 
        if not root:
            return None

        lnode = self.invertTree(root.left)
        rnode = self.invertTree(root.right)

        root.left, root.right = root.right, root.left
        
        return root

# @lc code=end

