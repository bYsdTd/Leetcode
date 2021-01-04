#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.cur = ["","","",""]
        self.curIndex = 0
        result = []
        n = len(s)
        def dfs(s:str, offset:int):
            # print("dfs", offset, self.curIndex, self.cur)
            if offset == n and self.curIndex == 4:
                result.append(self.cur[0]+"."+self.cur[1]+"."+self.cur[2]+"."+self.cur[3])
                return
            
            if (self.curIndex == 4 and offset < n) or (offset == n and self.curIndex < 4):
                return

            end = offset+1
            while end <= n:
                numstr = s[offset:end]
                num = int(numstr)
                if num > 255:
                    break
                self.cur[self.curIndex] = numstr
                self.curIndex += 1
                dfs(s, end)
                self.curIndex -= 1
                self.cur[self.curIndex] = ""
                if num == 0:
                    # 0开头不继续找了
                    break
                end += 1

            return
        
        dfs(s, 0)
        return result
# @lc code=end

