#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return 0
        
        result = []
        queue = [root]

        while queue:
            ql = len(queue)
            s = 0
            count = ql
            while count > 0:
                count -= 1
                c = queue.pop(0)
                s += c.val
                if c.left:
                    queue.append(c.left)
                if c.right:
                    queue.append(c.right)
            
            result.append(s/ql)

        return result
# @lc code=end

