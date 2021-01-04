#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        # 双指针，一个从头，一个从尾
        # 如果都是元音字符，就把两个值兑换
        # 如果不是元音字符，头部的就向后移动一个，尾部的就向头部移动一个
        # 直到两个指针相遇（这里相遇的条件是p1 >= p2,所以循环的条件是p1<p2
        # 不光是等于，因为有可能p1==p2的时候，两个都不是元音，那么都要移动，导致p2这时候就小于p1了）
        mp = set(('a','e','i','o','u','A','E','I','O','U'))
        p1 = 0
        p2 = len(s)-1
        ls = list(s)
        while p1 < p2:
            if ls[p1] in mp and ls[p2] in mp:
                # s = s[:p1]+s[p2]+s[p1+1:p2]+s[p1]+s[p2+1:len(s)]
                ls[p1], ls[p2] = ls[p2], ls[p1]
                p1 +=1
                p2 -=1
            else:
                if ls[p1] not in mp:
                    p1 += 1
                
                if ls[p2] not in mp:
                    p2 -= 1
            
        return "".join(ls)
# @lc code=end

