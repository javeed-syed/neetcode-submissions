class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        num = -heapq.heappop(self.maxHeap)
        heapq.heappush(self.minHeap, num)

        if len(self.minHeap) > len(self.maxHeap):
            curr = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -curr)

    def findMedian(self) -> float:
        m = len(self.maxHeap)
        n = len(self.minHeap)
        
        print([-i for i in self.maxHeap], self.minHeap)
        if m == n:
            return (self.minHeap[0] - self.maxHeap[0] ) / 2
        else:
            return float(-self.maxHeap[0])