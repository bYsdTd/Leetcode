#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resultDict = collections.defaultdict(list)
        for text in strs:
            hashIntValue = [0]*26
            for c in text:
                hashIntValue[ord(c)-ord('a')]+=1

            # for count in hashIntValue:
            #     hashValue.append(chr(count))

            resultDict[tuple(hashIntValue)].append(text)


        # result =[]
        # for v in resultDict.values():
        #     result.append(v)
        # return result
        return list(resultDict.values())

        # ans = collections.defaultdict(list)
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     ans[tuple(count)].append(s)
        # return list(ans.values())

# @lc code=end

