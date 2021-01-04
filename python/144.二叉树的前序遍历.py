#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 用一个栈保存遍历的节点
        # 先把右边的进栈，再把左边的进栈，保证左边先遍历
        
        # return self.preorder1(root)
        return self.preorder2(root)


    def preorder1(self, root: TreeNode) -> List[int]:
        if not root:
            return None

        result = []
        stack = [root]

        while stack:
            c = stack.pop()
            result.append(c.val)
            if c.right:
                stack.append(c.right)

            if c.left:
                stack.append(c.left)

        
        return result   

    def preorder2(self, root: TreeNode) -> List[int]:
        cur = root
        result = []
        stack = []
        while cur or stack:
            while cur:
                result.append(cur.val)
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            cur = cur.right

        return result
# @lc code=end

