#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # ----------------方案1 hashmap
        # 遍历每个元素
        # 目标值-当前值的结果去hashmap里找，如果找到的话，就返回hashmap的值和当前的索引
        # 如果不存在，把当前值做key，位置索引作为value存进去
        # mp = {}
        # for i in range(0, len(numbers)):
        #     remain = target - numbers[i]
        #     if remain in mp:
        #         return [mp[remain], i+1]
        #     else:
        #         mp[numbers[i]] = i+1
        
        # return None

        # ----------------方案2 双指针-----------------
        # 一个指针从头，一个指针从尾求和
        # 相等，返回结果
        # 大的话，移动尾部指针
        # 小的话，移动头部指针
        # 直到两个指针相遇

        p1 = 0
        p2 = len(numbers)-1
        while p1 != p2:
            s = numbers[p1] + numbers[p2]
            if s == target:
                return [p1+1, p2+1]
            elif s > target:
                p2 -=1
            else:
                p1+=1

        return None


# @lc code=end

