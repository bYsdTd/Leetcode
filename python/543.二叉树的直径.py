#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def depth(self, root: TreeNode) -> int:
        if root == None:
            return 0

        l = self.depth(root.left)
        r = self.depth(root.right)
        self.ans = max(self.ans, l+r+1)

        return max(l, r) + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        # 一定是在叶子末端节点中产生最大长度
        # 可以看成是每个节点左子树和右子树最大深度的和+1，就是当前节点为根的最大的节点个数
        # 然后每个节点都计算这个值，求最大的那个,
        # 最后的最后，这个过程是可以在计算深度的过程中，逐步的更新计算出来的
        # 也就是深度优先搜索的核心概念
        # 即，如果一个算法可以划分为左右子树，同时在左右子树的结果已经有了的情况下就可以计算的时候
        # 可以用递归的深度优先算法，在递归的过程中逐步的更新这个值
        # 因为递归退出到栈的某一层的时候，保证了这时左右子树的计算都已经完成

        self.depth(root)
        return self.ans-1
# @lc code=end

