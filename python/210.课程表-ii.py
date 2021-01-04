#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#

# @lc code=start
import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        return self.findOrderBfs(numCourses, prerequisites)

    def findOrderBfs(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 初始化边，计算入度
        indeg = [0] * numCourses
        edges = collections.defaultdict(list)
        for e in prerequisites:
            edges[e[1]].append(e[0])
            indeg[e[0]] += 1

        # 找出入度为0的，开始学习，就是加入结果队列，把相连接的入度-1
        # 如果入度为0，继续加入队列
        # 直到队列为空，如果学习过的课程与numCourses相同，就输出结果
        # 不可能的话返回空数组
        queue = [u for u in range(numCourses) if indeg[u] == 0]
        result = []
        while queue:
            cur = queue.pop(0)
            result.append(cur)
            if cur in edges:
                for i in edges[cur]:
                    indeg[i] -= 1
                    if indeg[i] == 0:
                        queue.append(i)

        return result if len(result) == numCourses else []

    
# @lc code=end

