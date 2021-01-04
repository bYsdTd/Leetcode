#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # 思路就是把一组数分成两组，让这两个不同的分别在不同的组
        # 然后再分别异或，就能找出不同的数
        # 全体异或，可以找出这两个数的异或结果，但是如果想要分成两组的话，只能根据其中某一位不同来分组
        # 这个某一位不同，可以通过diff ^= -diff来找出最右边的不同的位
        diff = 0
        for num in nums:
            diff ^= num
        result = [0, 0]
        diff &= -diff # 负数是取反+1
        for num in nums:
            if num & diff == 0:
                result[0] ^= num
            else:
                result[1] ^= num

        return result

# @lc code=end

