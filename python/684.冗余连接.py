#
# @lc app=leetcode.cn id=684 lang=python3
#
# [684] 冗余连接
#

# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 并查集实现
        # 对于一棵树来说，每一条新加入的边都增加了一个新的节点
        # 所以可以认为新的节点与老的节点是不联通的，也就是不在一个集合的
        # 如果新的节点也在老的集合里，说明找到了联通的边
        parent = [i for i in range(len(edges)+1)]
        # print("parent ", parent)

        # 并查集两种实现
        # def find(x:int) -> int:
        #     nonlocal parent
        #     return parent[x]

        # def union(x:int, y:int):
        #     u = find(x)
        #     v = find(y)
        #     if u == v:
        #         return

        #     for i in range(len(parent)):
        #         if parent[i] == u:
        #             parent[i] = v
        def find(x:int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            
            return parent[x]
        
        def union(x:int, y:int):
            u = find(x)
            v = find(y)
            if u == v:
                return
            parent[u] = v

        for e in edges:
            # print(e[0], e[1])
            if find(e[0]) == find(e[1]):
                return e
            
            union(e[0], e[1])

        return [-1, -1]

        
# @lc code=end

