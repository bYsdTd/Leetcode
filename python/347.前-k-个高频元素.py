#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.topKFrequentQuick(nums, k)
    
    def topKFrequentQuick(self, nums: List[int], k: int) -> List[int]:
        # 快排
        # 先统计出来每个字符出现的频率，保存在hashmap里
        fmp = {}
        frequentArray = []
        for num in nums:
            if num in fmp:
                fmp[num] += 1
            else:
                fmp[num] = 1

        for key in fmp:
            frequentArray.append(key)

        def partition(nums:List[int],lowIndex:int,highIndex:int) -> int:
            cur = lowIndex
            target = fmp[nums[highIndex]]
            for i in range(lowIndex, highIndex):
                if fmp[nums[i]] <= target:
                    nums[cur],nums[i] = nums[i], nums[cur]
                    cur += 1

            nums[cur],nums[highIndex] = nums[highIndex], nums[cur]
            return cur

        result = []
        def topKFre(nums:List[int], lowIndex:int, highIndex:int, topk:int):
            
            if highIndex < lowIndex:
                return
            
            # print("before", nums)
            qIndex = partition(nums, lowIndex, highIndex)
            # print("topKFre", lowIndex, highIndex, topk, qIndex)
            # print(nums)

            if highIndex-qIndex >= topk:
                topKFre(nums, qIndex+1, highIndex, topk)
            else:
                for i in range(qIndex, highIndex+1):
                    result.append(nums[i])
                topKFre(nums, lowIndex, qIndex-1, topk-highIndex+qIndex-1)

            return

        n = len(frequentArray)
        # print(fmp)
        topKFre(frequentArray, 0, n-1, k)

        return result
        
    def topKFrequentBucket(self, nums: List[int], k: int) -> List[int]:
        # 先统计出来每个字符出现的频率，保存在hashmap里
        fmp = {}
        maxFre = 0
        for num in nums:
            if num in fmp:
                fmp[num] += 1
            else:
                fmp[num] = 1
            maxFre = max(maxFre, fmp[num])
        
        # 创建桶,装入桶，用频率做桶的下标
        buckets = []
        for u in range(maxFre+1):
            buckets.append([])

        for value, f in fmp.items():
            buckets[f].append(value)

        # print(fmp, buckets)

        result = []
        count = 0
        for i in range(maxFre, -1, -1):
            for value in buckets[i]:
                result.append(value)
                count+=1
                if count == k:
                    return result
        
        return None

    def topKFrequentHeap(self, nums: List[int], k: int) -> List[int]:
        # 先统计出来每个字符出现的频率，保存在hashmap里
        fmp = {}
        for num in nums:
            if num in fmp:
                fmp[num] += 1
            else:
                fmp[num] = 1
        
        # 遍历hashmap中的元素，用hash的key做节点的值，用value的值来比较进行插入建堆
        # 小的值在顶端，保持堆的最大元素个数是k
        # 插入所有的元素结束后，堆里的元素就是出现频率最高的k个
        def heapify(nums:List[int], i:int, heapSize:int):
            l = 2 * i + 1
            r = 2 * i + 2
            minium = i
            if l < heapSize and fmp[nums[l]] < fmp[nums[minium]]:
                minium = l
            
            if r < heapSize and fmp[nums[r]] < fmp[nums[minium]]:
                minium = r
            
            if minium != i:
                nums[i], nums[minium] = nums[minium], nums[i]
                heapify(nums, minium, heapSize)

            return

        def heapInsert(nums:List[int], value:int, heapSize:int):
            # print("heapInsert", heapSize, nums)
            nums[heapSize] = value
            cur = heapSize
            while cur > 0:
                p = int((cur-1)/2)
                if fmp[nums[p]] > fmp[nums[cur]]:
                    nums[p], nums[cur] = nums[cur], nums[p]
                    cur = p
                else:
                    break
            return

        heapSize = 0
        result = [0] * k

        for value,f in fmp.items():
            if heapSize < k:
                heapInsert(result, value, heapSize)
                heapSize += 1
            else:
                if f > fmp[result[0]]:
                    result[0] = value
                    heapify(result, 0, heapSize)
                
        return result
# @lc code=end

