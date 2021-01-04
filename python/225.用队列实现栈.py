#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.deque1 = deque()
        self.deque2 = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if len(self.deque1) > 0 or len(self.deque2) == 0:
            self.deque1.append(x)
        elif len(self.deque2) > 0:
            self.deque2.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """

        if len(self.deque1) >= 1:
            while len(self.deque1) > 1:
                self.deque2.append(self.deque1.popleft())
            return self.deque1.popleft()
        elif len(self.deque2) >= 1:
            while len(self.deque2) > 1:
                self.deque1.append(self.deque2.popleft())            
            return self.deque2.popleft()


        return 0
        

    def top(self) -> int:
        """
        Get the top element.
        """    
        if len(self.deque1) >= 1:
            while len(self.deque1) > 1:
                self.deque2.append(self.deque1.popleft())
            topv = self.deque1[0]
            self.deque2.append(self.deque1.popleft())

        elif len(self.deque2) >= 1:
            while len(self.deque2) > 1:
                self.deque1.append(self.deque2.popleft())
            topv = self.deque2[0]
            self.deque1.append(self.deque2.popleft())
        
        return topv

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.deque1) == 0 and len(self.deque2) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

