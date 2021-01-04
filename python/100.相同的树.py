#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # DFS 递归的思想
        # 两个树相同，就是当前两个节点值相同，并且左子树和右子树的递归检查也相同
        if p and q:
            if p.val == q.val:
                result = self.isSameTree(p.left, q.left)
                if result:
                    return self.isSameTree(p.right, q.right)
                else:
                    return False
            else:
                return False
        
        if not p and not q:
            return True

        return False

        
# @lc code=end

