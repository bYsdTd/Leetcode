#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        return self.numSquaresDP(n)
        # return self.numSquaresBFS(n)

    def numSquaresDP(self, n: int) -> int:
        # dp算法
        # dp[i] 描述的是组成i需要的最少的平方数的个数, 那么给i减去一个平方数
        # 它需要的就是减去后的那个需要的平方数再加1
        # 但是i可以减去很多平方数, 减去的平方数小于i
        # 所以是这些dp(dp[i-1], dp[i-4], dp[i-9]......)里面最小的那个
        # while sq < i, j是平方数，1，4，9.。。。
        # dp[i] = dp[i-sq] + 1 ,取这个里面最小的一个
        squares = self.getSquares(n)
        dp = {}
        dp[0] = 0
        i = 1
        while i <= n:
            smallest = n
            for sq in squares:
                if sq <= i:
                    smallest = min(smallest, dp[i-sq])
                    # print("i:", i, "sq:", sq, "i-sq:", i-sq, "small", smallest)
                else:
                    break
            dp[i] = smallest + 1
            i +=1

        # print(dp)
        return dp[n]

    def numSquaresBFS(self, n: int) -> int:
        # BFS，节点到节点之间可以链接的意思就是他们的差是个平方数
        # 所以从n开始
        # n--- next1
        # | \
        # |   \
        # |     \
        # next2  next3
        # 每一个next 都是减去一个平方数得到的，
        # 那么最终如果能链接到节点0，并且是个最短路径，就可以找到这个最小值

        # BFS的图，经常是在运算过程中动态的更新的有哪些节点
        # 这道题的核心，就是把每次算出来的next作为节点放入队列了
        # 如果next小于0的话，这条路就结束了
        # 同时由于是广度优先，如果next之前已经处理过了，后面如果有新的next，他的深度肯定是比原来的大的，所以直接忽略掉
        marked = set()
        queue = [n]
        squares = self.getSquares(n)
        level = 0

        while queue:
            ql = len(queue)
            level +=1
            while ql > 0:
                ql -= 1
                cur = queue.pop(0)
                
                for s in squares:
                    nex = cur - s
                    if nex < 0:
                        break
                    
                    if nex == 0:
                        return level
                        
                    if nex in marked:
                        continue

                    marked.add(nex)
                    queue.append(nex)


        return n

    def getSquares(self, n: int) -> List[int]:
        squares = []
        t = n
        while n > 0:
            squares.append((t-n+1)*(t-n+1))
            n -=1
        
        return squares

# @lc code=end

