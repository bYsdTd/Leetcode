#
# @lc app=leetcode.cn id=424 lang=python3
#
# [424] 替换后的最长重复字符
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 两个指针，字典里记录两个最近出现的两个变量的次数，取其中最小的那个
        # 左边指针固定，右侧指针移动，如果右边的下一个指针的字符是下列情况

        maxLen = 0
        right = -1
        n = len(s)
        lookup = {}

        for i in range(n):
            while right+1 < n:
                nextchar = s[right+1]
                # print(i, right, lookup, maxLen)
                # print(s[right+1] == minikey and lookup[minikey] == k, dlen == 2, s[right+1] not in lookup)
                premaxCount = 0
                premaxKey = None
                for key, count in lookup.items():
                    if count > premaxCount:
                        premaxCount = count
                        premaxKey = key
                
                if len(lookup) > 0 and (nextchar not in lookup or nextchar != premaxKey):
                    remain = right+1-i+1-premaxCount
                    if remain > k:
                        break

                right += 1
                maxLen = max(maxLen, right-i+1)
                if s[right] in lookup:
                    lookup[s[right]] += 1
                else:
                    lookup[s[right]] = 1
            
            if s[i] in lookup:
                lookup[s[i]] -= 1
                if lookup[s[i]] == 0:
                    del lookup[s[i]]

        return maxLen


    def characterReplacementArrayMap(self, s: str, k: int) -> int:
        # 两个指针，字典里记录两个最近出现的两个变量的次数，取其中最小的那个
        # 左边指针固定，右侧指针移动，如果右边的下一个指针的字符是下列情况

        maxLen = 0
        right = -1
        n = len(s)
        lookup = [0] * 26
        offset = ord('A')
        for i in range(n):
            while right+1 < n:
                nextchar = s[right+1]
                # print(i, right, lookup, maxLen)
                # print(s[right+1] == minikey and lookup[minikey] == k, dlen == 2, s[right+1] not in lookup)
                premaxCount = 0
                premaxKey = 0
                for index in range(26):
                    if lookup[index] > premaxCount:
                        premaxCount = lookup[index]
                        premaxKey = index
                nextindex = ord(nextchar) - offset

                temp = lookup[nextindex] + 1
                
                if nextindex != premaxKey:
                    remain = right+1-i+1-premaxCount
                    if remain > k:
                        break

                right += 1
                maxLen = max(maxLen, right-i+1)
                lookup[ord(s[right])-offset] += 1
            
            lookup[ord(s[i])-offset] -= 1


        return maxLen
# @lc code=end

