#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
class NumArray:
    # 这里本质是先吧0-i-1的和求出来做个备忘，这样之后就直接减了
    def __init__(self, nums: List[int]):
        self.nums = nums
        n = len(nums)
        self.sums = [0] * (n+1)
        for i in range(1,n+1):
            self.sums[i] = nums[i-1] + self.sums[i-1]
        # print(self.sums)

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j+1] - self.sums[i]

    def sumRange1(self, i: int, j: int) -> int:
        n = len(self.nums)
        s = 0
        for index in range(i,j+1):
            if index >=0 and index <n:
                s += self.nums[index]
        return s


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end

