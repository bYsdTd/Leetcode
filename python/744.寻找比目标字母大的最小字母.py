#
# @lc app=leetcode.cn id=744 lang=python3
#
# [744] 寻找比目标字母大的最小字母
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # 二分查找，l,h, 需要考虑里面有重复出现的字母
        # 二分查找的关键点，循环中止条件
        # l <= h的话，最终h是要比l小的，最后一个循环肯定是l和h相等的
        # 
        # 如果这个时候的值比target大，就移动h（这时候l就是结果）
        # 如果比target小，就移动l（这时候l增大1以后的结果就是目标结果，
        # 但是这个时候有可能超过最大长度了，那么这时候就是第一个值）
        # 
        # 对于里面有重复元素的，就要考虑如果m与目标值相等的时候，是取左边，还是取右边
        # 由于是找比目标值大的，那么相等的时候，肯定应该取右边，那么应该是移动l的值
        # 所以把等于的处理放到< 目标值

        l=0
        n = len(letters)
        h = n-1

        while l <= h:
            m = l + int((h-l)/2)
            if ord(letters[m]) <= ord(target):
                l = m+1
            elif ord(letters[m]) > ord(target):
                h = m-1
        
        return letters[l] if l < n else letters[0]


            
# @lc code=end

