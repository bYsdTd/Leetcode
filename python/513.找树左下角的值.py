#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [root]
        result = 0
        while queue:
            result = queue[0].val
            ql = len(queue)
            while ql > 0:
                ql -= 1
                c = queue.pop(0)
                if c.left:
                    queue.append(c.left)
                if c.right:
                    queue.append(c.right)
        
        return result
# @lc code=end

