#
# @lc app=leetcode.cn id=241 lang=python3
#
# [241] 为运算表达式设计优先级
#

# @lc code=start
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        return self.diffWaysToCompute2(input)

    def diffWaysToCompute2(self, input: str) -> List[int]:
        # 思路还可以更简洁
        # 递归的方法就是一种找到符号，两边细分
        # 如果没有找到符号，就把当前字符串直接加入结果

        opset = ("+", "-", "*")
        def partitionCompute(formula:str, begin:int, end:int) -> List[int]:

            result = []
            hasOp = False
            for i in range(begin,end+1):
                op = formula[i]
                if op in opset:
                    preResult = partitionCompute(formula, begin, i-1)
                    postResult = partitionCompute(formula, i+1, end)
                    hasOp = True
                    
                    if op == "+":
                        for pre in preResult:
                            for post in postResult:
                                result.append(pre+post)
                    elif op == "-":

                        for pre in preResult:
                            for post in postResult:
                                result.append(pre-post)
                    elif op == "*":

                        for pre in preResult:
                            for post in postResult:
                                result.append(pre*post)
            
            if not hasOp:
                return [(int(formula[begin:end+1]))]

            return result

        return partitionCompute(input, 0, len(input)-1)         

    def diffWaysToCompute1(self, input: str) -> List[int]:
        # 以某一个符号开始分成两段，每一段分别计算结果，然后再用符号运算
        # 从头开始遍历所有的符号，做这个运算
        opset = ("+", "-", "*")
        result = []

        def partitionCompute(input:str, begin:int, end:int) ->List[int]:
            opIndex = -1
            r = []
            hasopinstr = False
            for i in range(begin, end):
                if input[i] in opset:
                    hasopinstr = True
                    opIndex = i
                    
                    hasOp = False
                    prenum = []
                    
                    for i in range(begin, opIndex):
                        if input[i] in opset:
                            hasOp = True
                            break
                    
                    if hasOp:
                        prenum += (partitionCompute(input, begin, opIndex-1))
                    else:
                        prenum.append(int(input[begin:opIndex]))

                    
                    hasOp = False
                    postnum = []
                    for i in range(opIndex+1, end):
                        if input[i] in opset:
                            hasOp = True
                            break
                    
                    if hasOp:
                        postnum += (partitionCompute(input, opIndex+1, end))
                    else:
                        postnum.append(int(input[opIndex+1:end+1]))


                    for pre in prenum:
                        for post in postnum:
                            t = 0
                            if input[opIndex] == '+':
                                t = pre + post
                            elif input[opIndex] == '-':
                                t = pre - post
                            elif input[opIndex] == '*':
                                t = pre * post
                            
                            r.append(t)

            if not hasopinstr:
                r.append(int(input[begin:end+1]))
            return r

        n = len(input)
        result = partitionCompute(input, 0, n-1)

        return result
# @lc code=end

