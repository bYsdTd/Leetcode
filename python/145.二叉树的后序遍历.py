#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder1(self, root: TreeNode) -> List[int]:
        if not root:
            return None

        result = []
        stack = [root]

        while stack:
            c = stack.pop()
            result.append(c.val)
            if c.left:
                stack.append(c.left)
            
            if c.right:
                stack.append(c.right)

        result.reverse()

        return result

    def postorder2(self, root: TreeNode) -> List[int]:

        # 栈数据模拟递归的大体思路
        # 1 每拿到一个 节点 就把它保存在 栈 中
        # 2 继续对这个节点的 左子树 重复 过程1，直到左子树为 空
        # 3 因为保存在 栈 中的节点都遍历了 左子树 但是没有遍历 右子树，
        # 所以对栈中节点 出栈 并对它的 右子树 重复 过程1
        # 4 直到遍历完所有节点

        result = []
        stack = []
        cur = root
        pre = None

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            if not cur.right or cur.right == pre:
                result.append(cur.val)
                pre = cur
                cur = None
            else:
                stack.append(cur)
                cur = cur.right
        
        return result




    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # return self.postorder1(root)
        return self.postorder2(root)
# @lc code=end

