#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:
    
    # 最小值栈，用一个额外的栈来维护最小值
    # 与原始栈同步的操作，相当于实时的记录下，栈顶每一时刻的最小值
    # 这样相当于每次最小值栈的栈顶就是最小的元素

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []
        self.min = sys.maxsize

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min = min(self.min, x)
        self.minStack.append(self.min)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        # 当前最小值是当前的minstack的栈顶
        n = len(self.minStack)
        self.min = self.minStack[n-1] if n >=1 else sys.maxsize

    def top(self) -> int:
        n = len(self.minStack)
        return self.stack[n-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

