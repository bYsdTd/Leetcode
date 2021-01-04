#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 与下一个更高温度类似，但是由于是循环的
        # 所以栈还是用来保存当前已经遍历过的节点，并且如果是已经找到更大的话，就弹出栈
        # 但是由于是循环的，所以存在遍历到最后已经压栈的存在前面有比他大的
        # 这里的策略是再遍历一遍，来找到是否在前面还有比他大的

        n = len(nums)
        result = [-1]*n
        indexStack = []
        
        for curIndex in range(0, 2*n):
            num = nums[curIndex%n]

            while len(indexStack) > 0 and num > nums[indexStack[len(indexStack)-1]]:
                pre = indexStack.pop()
                result[pre] = num

            if curIndex < n:
                indexStack.append(curIndex)
        
        return result
# @lc code=end

