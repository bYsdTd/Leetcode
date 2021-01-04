#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindromeStr(self, x: int) -> bool:
        # 转成字符串
        # n个字符，只需要比较n/2次头和尾是否相同
        s = str(x)
        n = len(s)
        
        for i in range(int(n/2)):
            if s[i] != s[n-i-1]:
                return False
        
        return True
    
    def isPalinadromeNum(self, x: int) -> bool:
        # 先计算出总共多少位数
        # 取出前面的部分和余数的部分,分奇偶数
        # 然后把其中一个翻转一下，看与另一个是否相等
        
        if x < 0:
            return False
        l = 0
        temp = x
        while temp > 0:
            l += 1
            temp = int(temp/10)

        childLen = int(l/2)

        right = x % (pow(10, childLen))

        left = int(x / int(pow(10, l-childLen)))

        leftRerverse = 0
        for i in range(childLen):
            leftRerverse += int(left/pow(10,i) % 10) * int(pow(10, (childLen-i-1)))

        return leftRerverse == right

    def isPalinadromeNum2(self, x: int) -> bool:

        if x == 0:
            return True
            
        if x < 0 or x % 10 == 0:
            return False
        right = 0

        while x > right:
            right = right * 10 + x % 10
            x = int(x /10)

        return right == x or x == int(right/10)

    def isPalindrome(self, x: int) -> bool:
        # return self.isPalindromeStr(x)
        return self.isPalinadromeNum2(x)

    
# @lc code=end

