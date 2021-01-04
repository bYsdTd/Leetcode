#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # m 如果是错误版本，说明第一个错误在前面，h=m
        # m 如果不是错误版本，说明错误版本在后面，l=m+1
        # l==h 结束,那么最后一次是剩下两个，要么都是错，要么是对，错
        # 如果都是错，m指向第一个，这时候，l=h=m都指向错的那个
        # 如果第一个对的，m指向的是对的，l=m+1 l指向的是错的那个

        l = 1
        h = n
        while l < h:
            m = l + int((h-l)/2)
            if isBadVersion(m):
                h = m
            else:
                l = m+1
        
        return l

# @lc code=end

