#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
class Solution:

    # 正向思维是把节点判定是否与字典里的所有节点都有关联
    # 但是这样的问题是，在字典非常大的时候，时间复杂度不允许
    # 那么改成修改当前节点单词的每一位，然后再去字典里找，判定是否能连接
    # 还是动态构建的过程

    # def ladderLength1(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     st=set(wordList)
    #     if endWord not in st:
    #         return 0
    #     m=len(beginWord)        

    #     queue=collections.deque()        
    #     queue.append((beginWord,1))

    #     visited=set()
    #     visited.add(beginWord)

    #     while queue:
    #         cur,step=queue.popleft()
    #         if cur==endWord:
    #             return step
            
    #         for i in range(m):                
    #             for j in range(26):
    #                 tmp=cur[:i]+chr(97+j)+cur[i+1:]
    #                 if tmp not in visited and tmp in st:
    #                     queue.append((tmp,step+1))
    #                     visited.add(tmp)

    #     return 0
   
    # 预先构建图的情况，时间复杂度超了
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 单词到单词之间如果只有一个字母不同，就认为是可以是有路径的
        # 最短转化，就是BFS下的最短路径
        # 中间每个单词都是一个路径上的节点
        # 同样是用队列管理，每次取出一层来遍历

        # 效率的问题，这里有个处理，就是要预先构建好图，而不是运行时构建

        level = 0
        queue = [beginWord]
        marked = set()
        st = set(wordList)
        m = len(beginWord)

        if endWord not in st:
            return 0
            
        # 预先构建图的情况，时间复杂度超了
        #self.buildGraphic(wordList) 

        while queue:
            ql = len(queue)
            level +=1
            while ql > 0:
                ql -=1
                cur = queue.pop(0)

                if cur == endWord:
                    return level
                
                if cur in marked:
                    continue
                
                marked.add(cur)

                # 去字典里找能转换的单词
                for i in range(m):
                    for j in range(26):
                        tmp=cur[:i]+chr(97+j)+cur[i+1:]
                        if tmp not in marked and tmp in st:
                            queue.append(tmp)
        return 0 

    # def canChange(self, a:str, b:str) -> bool:
    #     c = 0
    #     n = len(a)
    #     i = 0

    #     while i < n and c <=1:
    #         if a[i] != b[i]:
    #             c += 1
    #         i +=1
        
    #     return c==1

    # def buildGraphic(self, wordList: List[str]) -> dict:

    #     # 用索引
    #     n = len(wordList)
    #     self.graphic = []
    #     for i in range(n):
    #         self.graphic.append([0]*n)

    #     for i in range(n):
    #         for j in range(n):
    #             if not self.graphic[i][j] and self.canChange(wordList[i], wordList[j]):
    #                 self.graphic[i][j] = 1
    #                 self.graphic[j][i] = 1

    #     return self.graphic
# @lc code=end

