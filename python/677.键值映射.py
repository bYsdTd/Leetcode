#
# @lc app=leetcode.cn id=677 lang=python3
#
# [677] 键值映射
#

# @lc code=start
class Node:
    def __init__(self):
        self.next = [None for _ in range(26)]
        self.val = 0
        return
        
class MapSum:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for c in key:
            i = ord(c)-ord('a')
            if not node.next[i]:
                node.next[i] = Node()
            node = node.next[i]
        
        node.val = val
        return

    def sum(self, prefix: str) -> int:
        self.s = 0
        def sum(node:Node, pre:str):
            if not node:
                return

            n = len(pre)
            if n == 0:
                self.s += node.val
                for nex in node.next:
                    sum(nex, "")
            else:
                i = ord(pre[0]) - ord('a')
                sum(node.next[i], pre[1:])

        sum(self.root, prefix)
        return self.s
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
# @lc code=end

