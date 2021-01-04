#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        self.result = 0
        self.count = 0
        def inTravers(root: TreeNode) -> bool:
            if not root:
                return False

            if inTravers(root.left):
                return True
            
            self.count += 1
            if k == self.count:
                self.result = root.val
                return True
            
            
            return inTravers(root.right)
        
        
        inTravers(root)
        return self.result
# @lc code=end

