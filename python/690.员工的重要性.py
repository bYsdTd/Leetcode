#
# @lc app=leetcode.cn id=690 lang=python3
#
# [690] 员工的重要性
#

# @lc code=start
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        # DFS，递归实现
        # cur = None
        # for e in employees:
        #     if e.id == id:
        #         cur = e
        #         break

        # if not cur:
        #     return 0

        # imp = cur.importance
        # for c in cur.subordinates:
        #     imp += self.getImportance(employees, c)

        # return imp

        # BFS, 队列实现
        queue = [id]
        s = 0

        mp = {}
        for e in employees:
            mp[e.id] = e

        while queue:
            curId = queue.pop(0)
            s += mp[curId].importance
            for c in mp[curId].subordinates:
                queue.append(c)

        return s
# @lc code=end

