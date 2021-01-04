#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N叉树的最大深度
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # DFS 递归
        # if not root:
        #     return 0
        
        # md = 0
        # for c in root.children:
        #     d = self.maxDepth(c)
        #     md = max(d, md)

        # return md+1

        # 队列实现
        if not root:
            return 0
            
        queue = [root]

        level = 0
        while queue:
            n = len(queue)
            while n > 0:
                n-=1
                curNode = queue.pop(0)
                for c in curNode.children:
                    queue.append(c)

            level +=1

        return level

        
# @lc code=end

