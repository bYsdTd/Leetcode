#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.instack = []
        self.outstack = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while len(self.outstack)>0:
            list.append(self.instack, list.pop(self.outstack))

        list.append(self.instack, x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while len(self.instack) >0:
            list.append(self.outstack, list.pop(self.instack))

        return self.outstack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        while len(self.instack) >0:
            list.append(self.outstack, list.pop(self.instack))

        return self.outstack[len(self.outstack)-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """

        return len(self.instack) == 0 and len(self.outstack) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

