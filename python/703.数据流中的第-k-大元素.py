#
# @lc app=leetcode.cn id=703 lang=python3
#
# [703] 数据流中的第 K 大元素
#

# @lc code=start
class KthLargest:

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
        
        if heapSize >= len(heap):
           heap.append(num)
        else:
            heap[i] = num

        while i > 0:
            parent = int((i-1)/2)
            if heap[parent] > heap[i]:
                heap[parent], heap[i] = heap[i], heap[parent]
                i = parent
            else:
                break
    # 最小堆相关实现end

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        self.heap = [0] * len(nums)
        self.heapSize = 0

        for num in nums:
            self.insertHeap(self.heap, num, self.heapSize)
            self.heapSize += 1
            if self.heapSize > self.k:
                self.extractMin(self.heap, self.heapSize)
                self.heapSize-=1

    def add(self, val: int) -> int:
        self.insertHeap(self.heap, val, self.heapSize)
        self.heapSize += 1
        if self.heapSize > self.k:
            self.extractMin(self.heap, self.heapSize)
            self.heapSize-=1

        return self.heap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

