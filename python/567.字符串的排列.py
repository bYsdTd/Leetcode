#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 以s1的长度建立滑动窗口，放在s2上开始比较
        # 用一个hashmap记录每个字符出现的次数，如果s1和s2窗口内的内容完全匹配，就找到了
        n1 = len(s1)
        n2 = len(s2)
        right = n1-1
        lookup2 = {}
        lookup1 = {}
        if n2 < n1:
            return False
            
        for i in range(n1):
            if s2[i] in lookup2:
                lookup2[s2[i]] += 1
            else:
                lookup2[s2[i]] = 1
            
            if s1[i] in lookup1:
                lookup1[s1[i]] += 1
            else:
                lookup1[s1[i]] = 1

        for i in range(n2-n1+1):
            same = True
            for j in range(n1):
                if s1[j] not in lookup2 or lookup1[s1[j]] != lookup2[s1[j]]:
                    same = False
                    break
            if same:
                return True

            right += 1
            lookup2[s2[i]] -= 1
            if right < n2:
                if s2[right] in lookup2:
                    lookup2[s2[right]] += 1
                else:
                    lookup2[s2[right]] = 1
            
        return False

# @lc code=end

