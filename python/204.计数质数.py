#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        # 从2开始遍历，把i的倍数都去掉
        # 同时，检查的时候，从i*i检查就可以了，因为i前面的倍数已经检查过了
        # 比如检查3的倍数的时候，从9开始就行，因为6已经在检查2的时候检查过了
        count = 0
        lookup = [0] * n
        for i in range(2,n):
            if lookup[i]:
                continue
            count += 1
            for j in range(i*i,n,i):
                lookup[j] = 1
        
        return count
# @lc code=end

