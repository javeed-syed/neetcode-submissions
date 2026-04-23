class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        nums = [-num for num in nums]
        heapq.heapify(nums)
        self.heap = nums
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        temp = []
        for _ in range(self.k):
            k = heapq.heappop(self.heap)
            temp.append(k)
        ans = - temp[-1]
        for num in temp:
            heapq.heappush(self.heap, num)
        return -k