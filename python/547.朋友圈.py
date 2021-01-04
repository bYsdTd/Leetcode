#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#

# @lc code=start
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # DFS，从0开始遍历每一个人的朋友圈，向后DFS遍历
        # 比如从0开始的朋友圈，就看1是不是它的朋友，如果是的话就继续找1的朋友圈
        # 已经处理过的加入visit列表，不需要重复处理
        # 每一层dfs结束，就朋友圈计数+1
        self.visited = set()
        self.n = len(M)
        circleNum = 0
        for i in range(self.n):
            if i in self.visited:
                continue
            circleNum +=1
            self.DFSFriend(M, i)
        
        return circleNum


    def DFSFriend(self, M: List[List[int]], p:int) -> None:
        # DFS 找p的朋友圈，如果是朋友圈里的就加入visited
        self.visited.add(p)
        for i in range(self.n):
            if i in self.visited:
                continue
            if M[p][i]:
                self.visited.add(i)
                self.DFSFriend(M,i)


# @lc code=end

