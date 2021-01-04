#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # 同样递归思想
        # 缩小范围计算，分别合并左子树和右子树
        # 如果当前两个节点都不空，相加，否则的话，直接把非空的那个作为合并后的节点（包含了后续的左右子节点）
        # 先从根节点合并，就是先序遍历
        # 考虑是深度优先搜索，所以在递归结束后再修改t1的left和right的值，不会对递归有什么影响
        # 因为left和right都已经出栈了

        if not t1 and not t2:
            return None

        if not t1:
            return t2
        elif not t2:
            return t1

        t1.val += t2.val

        l = self.mergeTrees(t1.left, t2.left)
        r = self.mergeTrees(t1.right, t2.right)

        t1.left = l
        t1.right = r

        return t1

# @lc code=end

