#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        return self.count2(s)

    # O(n)
    def count2(self, s: str) -> int:
        # 从头遍历,用一个pre值记录上一个连续相同的个数是多少
        # cur记录的是当前连续的count
        # cur 大于等于pre的时候，就找到一个
        preCount, curCount, count =0 , 1, 0

        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                curCount += 1
            else:
                preCount = curCount
                curCount = 1
            
            if preCount >= curCount:
                count += 1
        
        return count

    # 超时 O(n^2)
    def count1(self, s: str) -> int:
        # 分别以第0位，第1位，第xxxx位为起点，找01的组合
        # pre表示当前的前字符，count表示在前面出现的次数
        # 找到是否后面有连续的与pre相反的字符
        count = 0
        n = len(s)

        # 当前begin开始，是否有符合的字符串
        def search(s:str, begin:int, n:int) -> bool:
            if begin < 0 or begin>= n:
                return False
            cur = s[begin]
            c = 0

            while begin < n and s[begin] == cur:
                c += 1
                begin += 1

            while begin < n and s[begin] != cur and c > 0:
                c -= 1
                begin += 1

            return c == 0

        # 循环遍历求解
        for i in range(len(s)):
            count += 1 if search(s, i, n) else 0

        return count

# @lc code=end

