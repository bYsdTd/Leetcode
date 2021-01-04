#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # 扫描字符串，维护一个栈
        # 拿出一个字符串，与栈顶的字符比较
        # 如果匹配的话，就把栈顶弹出
        # 如果不匹配的话，就把新的字符压栈
        # 最后扫描完，如果栈是空的，就是匹配的
        stack = []
        mp = {'(':')', '{':'}', '[':']'}
        for c in s:
            n = len(stack)
            if n > 0:
                top = stack[n-1]
                if top in mp and mp[top] == c:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)

        return len(stack) == 0

# @lc code=end

