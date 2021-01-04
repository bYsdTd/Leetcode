#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # edge list 表示的有向图
        # 问题转变成检测有向图有没有环
        return self.isGraphCircleBFS(numCourses, prerequisites)

    def isGraphCircleBFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        # 广度优先搜索的思路
        # 如果一门课程的入度为0，就表示这门课程可以修了
        # 那么先统计出来所有课程的入度，然后找出入度为0的
        # 学习之，然后这门课程学完了，相邻的课程的入度就都减1
        # 减1之后如果入度也为0了，就可以加入待学习的课程了
        # 这样操作，直到待学习的课程的队列为空，就是学完了
        # 如果最后学完的课程的数量==numCourses，就说明学完了
        indeg = [0] * numCourses
        for e in prerequisites:
            edges[e[1]].append(e[0])
            indeg[e[0]] += 1

        q = [u for u in range(numCourses) if indeg[u] == 0]
        learned = []
        while q:
            cur = q.pop(0)
            learned.append(cur)
            if cur in edges:
                for adj in edges[cur]:
                    indeg[adj] -= 1
                    if indeg[adj] == 0:
                        q.append(adj)
        
        return len(learned) == numCourses


    def isGraphCircleDFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 有环的话，遍历最终会遍历回已经遍历过的节点
        # edge list表示的图要如何遍历
        # 把每个边的目标点保存到集合里，
        # 如果新的边的起点在集合中，判定终点在集合中就有环，不在集合中，就把
        
        # edgelist 转变成邻接表的形式，然后分别通过dfs和bfs遍历，
        # 对dfs遍历过的节点有几种状态值
        # 0 还没遍历，
        # 1访问到了，但是递归还没出栈，
        # 2 递归已经出栈
        # 对于有向图来说，对于遍历过程中遇到的边的另一个节点，如果状态是1，就是目前还没出栈的
        # 就说明有环了

        # 这里用dfs
        edges = collections.defaultdict(list)
        for e in prerequisites:
            edges[e[1]].append(e[0])
        
        visited = [0] * numCourses

        def dfs(p:int) -> bool:
            visited[p] = 1
            for e in edges[p]:
                if visited[e] == 1:
                    return False
                else:
                    if not dfs(e):
                        return False

            visited[p] = 2
            return True
        
        for i in range(numCourses):
            if visited[i] != 2:
                if not dfs(i):
                    return False

        # print(edges)
        return True
            

# @lc code=end

