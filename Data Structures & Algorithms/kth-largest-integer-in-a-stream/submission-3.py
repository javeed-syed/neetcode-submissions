class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap, self.k = nums, k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        print(f"Current heap elements")

    def add(self, val: int) -> int:
        print(f"Adding number {val} to the heap.")
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]