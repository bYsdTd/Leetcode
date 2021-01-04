#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # 用一个栈来维护当前遍历过的温度的索引位置，如果比栈顶的温度高，说明找到了后面的比前面的高的第一个温度
        # 栈顶肯定永远是栈里面最小的温度，这样如果比栈顶低，肯定就比前面的都要低
        # 就需要继续往后找到更高的
        # 如果比栈顶温度高，就弹出栈，继续往里面找，直到当前的温度更低，就继续压栈
        
        # 算法
        # 遍历数组
        # 一直取栈顶的元素，直到当前值比栈顶元素小，大的话，就更新栈顶元素的距离
        # 当前的索引压入栈

        n = len(T)
        result = [0]*n
        indexStack = []

        for curIndex in range(0,n):
            while len(indexStack) > 0 and T[indexStack[len(indexStack)-1]] < T[curIndex]:
                preIndex = indexStack.pop()
                result[preIndex] = curIndex - preIndex
                

            indexStack.append(curIndex)

        return result
        
# @lc code=end

