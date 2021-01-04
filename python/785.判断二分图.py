#
# @lc app=leetcode.cn id=785 lang=python3
#
# [785] 判断二分图
#

# @lc code=start
# 并查集

class Solution:

    def isBipartite(self, graph: List[List[int]]) -> bool:
        return self.isBipartiteUnionFind(graph)

    def isBipartiteUnionFind(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        p = [i for i in range(n)]

        def find(x):
            nonlocal p
            if p[x]!= x:
                p[x]=find(p[x])
            return p[x]
        
        # 合并就是把y的父亲设置成x的父亲
        def merge(x:int, y:int) -> bool:
            nonlocal p
            p1 = find(x)
            p2 = find(y)
            p[p2] = p1
        
        for i, g in enumerate(graph):
            # 把i邻接的所有节点合并到一起，看是否能合并成功
            ip = find(i)
            for other in g:
                if find(other) == ip:
                    return False

            if g:
                c = g[0]
                for j in g[1:]:
                    merge(c, j)

        return True
            

    def isBipartiteDfs(self, graph: List[List[int]]) -> bool:
        marked = set()
        a = set()
        b = set()
        def dfs(graph:List[List[int]], start:int) -> bool:
            # visit
            # 当前节点如果没有访问过，就检测下
            # if start not in marked:
                # print(start)
            marked.add(start)
            if start not in a and start not in b:
                a.add(start)
            
            # 找出当前节点的集合和邻接节点的集合分别是哪个
            adj = b if start in a else a
            sel = a if start in a else b
            
            result = True
            for c in graph[start]:
                # 对邻接的节点判定，如果没有处理过，就继续递归dfs
                # 同时如果没有加入集合的话，就加入相邻的集合
                if c not in marked:                    
                    if c not in sel:
                        adj.add(c)
                    if not dfs(graph, c):
                        return False
                    # result = dfs(graph, c) and result
                else:
                # 判定是否冲突
                # 因为有可能之前已经在mark的集合里了，所以需要在外部判定
                    if c in sel:
                        return False

            return result

        for i in range(len(graph)):
            # 以每个节点为开始，dfs遍历，如果中间有冲突，就返回
            if not dfs(graph, i):
                return False

        return True

    def isBipartiteBfs(self, graph: List[List[int]]) -> bool:
        queue = []
        marked = set()
        a = set()
        b = set()

        for i in range(len(graph)):
            if i not in marked:
                queue.append(i)
            
            while queue:
                cur = queue.pop(0)
                # if cur not in marked:
                    # print(cur)
                    # 遍历到的节点，加入到集合中
                marked.add(cur)
                if cur not in a and cur not in b:
                    a.add(cur)
                
                adj = b if cur in a else a
                sel = a if cur in a else b

                # 相邻的节点，如果是在cur相同的集合中，就冲突了，返回失败
                # 否则的话，加入不同的那个集合
                # 同时加入队列，进行下一层的迭代

                for c in graph[cur]:
                    if c not in marked:
                        queue.append(c)
                        if c in sel:
                            return False
                        else:
                            adj.add(c)

        return True
# @lc code=end

