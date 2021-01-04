#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = []
        self.curpath = []
        def dfs(root: TreeNode):
            if not root:
                return

            self.curpath.append(root.val)
            if not root.left and not root.right:
                path = ""
                n = len(self.curpath)
                for i in range(n):
                    path += str(self.curpath[i])
                    if i != n-1:
                         path += "->"
                result.append(path)
                self.curpath.pop()
                return

            dfs(root.left)
            dfs(root.right)
            self.curpath.pop()
            return
        
        dfs(root)
        return result
# @lc code=end

