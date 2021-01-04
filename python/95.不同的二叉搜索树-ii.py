#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.generateTrees1(n)

    def generateTrees1(self, n: int) -> List[TreeNode]:
        
        # def partition(begin:int, end:int) -> List[TreeNode]:
            
        #     if end == begin:
        #         return [TreeNode(begin)]
        #     elif end < begin:
        #         return None

        #     result = []
        #     for i in range(begin, end+1):
        #         left = partition(begin, i-1)
        #         right = partition(i+1, end)

        #         # print(begin, end, left, right)

        #         if left and right:
        #             for l in left:
        #                 for r in right:
        #                     root = TreeNode(i)
        #                     result.append(root)
        #                     root.left = l
        #                     root.right = r
        #         elif left:
        #             for l in left:
        #                 root = TreeNode(i)
        #                 result.append(root)
        #                 root.left = l
        #         elif right:
        #             for r in right:
        #                 root = TreeNode(i)
        #                 result.append(root)
        #                 root.right = r

        #     return result

        def partition(begin:int, end:int) -> List[TreeNode]:
            
            if end < begin:
                return [None]

            result = []
            for i in range(begin, end+1):
                left = partition(begin, i-1)
                right = partition(i+1, end)

                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        result.append(root)
                        root.left = l
                        root.right = r


            return result

        if n < 1:
            return []
        r = partition(1,n)
        return r


# @lc code=end

