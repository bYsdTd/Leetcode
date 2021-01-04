#
# @lc app=leetcode.cn id=1091 lang=python3
#
# [1091] 二进制矩阵中的最短路径
#

# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # BFS 标准队列求解过程
        # 队列不空的情况下，取出当前这一层的所有节点，遍历周围的节点，继续加入队列
        # 当前路径层数+1
        # 这里有个巧妙的地方，就是直接用grid的数据来标记是否已经走过了
        # 相当于修改了原始数据
        # BFS的核心是，当前层的每个节点拿出来，先判定当前这个节点是否是阻挡（与是否已经走过是同一个判定条件）
        # 然后判定当前是不是已经到终点了（先判定上面的已经保证了当前不是阻挡）所以终点是可走的，返回路径长度

        offset = [[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0]]
        queue = [[0,0]]
        pathLength = 0
        n = len(grid)


        mp = []
        for i in range(n):
            mp.append([0]*n)

        if grid[0][0]:
            return -1

        while queue:
            curLevelCount = len(queue)
            pathLength +=1

            while curLevelCount:
                curLevelCount -=1
                node = queue.pop(0)
                
                row =node[0]
                col = node[1]
                
                # # 标记已经走过
                # if mp[row][col]:
                #     continue
                
                # 阻挡不能走
                if grid[row][col]:
                    continue
                
                if row == n-1 and col == n-1:
                    return pathLength

                # 标记
                grid[row][col]=1

                for o in offset:
                    x=node[0]+o[0]
                    y=node[1]+o[1]

                    if x<0 or x >=n or y<0 or y>=n:
                        continue

                    c = grid[x][y]
                    
                    if not c:
                        queue.append([x,y])
                
               
                
        return -1

# @lc code=end

