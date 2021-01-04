#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:

    # 找到两个子节点中比当前小的
    # 然后交换，再递归去比较交换后的子节点
    # heapify的前提是，两个子堆都已经是调整好的堆

    # 最小堆相关实现
    def heapify(self, heap:List[int], i:int, heapSize:int) -> None:
        c1 = 2*i+1
        c2 = 2*i+2
        smallest = i

        if c1 < heapSize and heap[c1] < heap[smallest]:
            smallest = c1
        
        if c2 < heapSize and heap[c2] < heap[smallest]:
            smallest = c2

        if smallest != i:
            heap[smallest], heap[i] = heap[i], heap[smallest]
            self.heapify(heap, smallest, heapSize)

    def extractMin(self, heap:List[int], heapSize:int) -> None:
        if heapSize > 0:
            heap[0], heap[heapSize-1] = heap[heapSize-1], heap[0]
            self.heapify(heap, 0, heapSize-1)

    def insertHeap(self, heap:List[int], num:int, heapSize:int) -> int:
        # 不断与父节点比较，直到父节点比自己还小
        i = heapSize
        heap[i] = num
        while i > 0:
            parent = int((i-1)/2)
            if heap[parent] > heap[i]:
                heap[parent], heap[i] = heap[i], heap[parent]
                i = parent
            else:
                break
    # 最小堆相关实现end

    # 方案1, 堆实现
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        # 小顶堆，不断向里插入，如果堆里元素大于k个，就移除堆顶元素
        # 注意这里是先插入优先队列，再判定大于k个，因为你不确定新来的是不是比堆顶的大，如果大的话，新来的应该是要移除的
        # 堆里时刻保持k个最大的元素
        heap = [0] * len(nums)
        heapSize = 0

        for num in nums:
            self.insertHeap(heap, num, heapSize)
            heapSize += 1
            if heapSize > k:
                self.extractMin(heap, heapSize)
                heapSize-=1

        return heap[0]

    # 方案2，快排
    # 分解的步骤，选定一个值，把比他小的值交换到左边
    # 用一个指针标记当前小的部分的值覆盖到哪里了
    # 遍历整个数组
    def partition(self, nums:List[int], l:int, h:int) -> int:
        i=l
        for j in range(l,h):
            if nums[j] < nums[h]:
                nums[j],nums[i] = nums[i], nums[j]
                i+=1
        nums[i], nums[h] = nums[h], nums[i]

        return i

    # 计算出索引是k的值就结束
    def quickSort(self, nums:List[int], k:int, l:int, h:int) -> int:
        if l>=h:
            return -1

        q = self.partition(nums, l, h)

        if q == k:
            return q
        
        result = self.quickSort(nums, k, l, q-1)
        if result >=0:
            return result

        result = self.quickSort(nums, k, q+1, h)

        return result

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        # 快排的过程中，由于每次分解后的中间值，就是最终的位置，所以有可能中间就算出倒数第k个值得位置了
        n = len(nums)
        k = n-k
        result = self.quickSort(nums, k, 0, n-1)
        if result < 0:
            return nums[k]
        else:
            return nums[result]

    # git hub 算法
    def partition2(self, a:List[int] , l:int, h:int) -> int:
        i = l
        j = h + 1
        while True:
            i+=1
            
            while a[i] < a[l] and i < h:
                i+=1
            
            j-=1    
            while a[j] > a[l] and j > l:
                j-=1

            if i >= j:
                break
            a[i], a[j] = a[j], a[i]
        
        a[l], a[j] = a[j], a[l]
        return j


    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        k = n - k
        l = 0
        h = n - 1

        while l < h:
            j = self.partition2(nums, l, h)
            if j == k:
                break
            elif j < k:
                l = j + 1
            else:
                h = j - 1
            
        return nums[k]
# @lc code=end

