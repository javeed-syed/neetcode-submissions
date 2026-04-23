class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque([])
        heap = []

        counter = Counter(tasks)

        for task, count in counter.items():
            heapq.heappush(heap, (-count, task))
        
        time = 0

        print(f"init heap: {heap}")
        while heap or queue:
            time += 1

            if len(heap) > 0:
                curr = heapq.heappop(heap)
                count, task = curr
                count *= -1
                if count > 1:
                    count -= 1
                    queue.append((time + n, task, count))
                print(task, end=" -> ")
            else:
                print("Idle", end=" -> ")

            if queue and time == queue[0][0]:
                _, task, count = queue.popleft()
                heapq.heappush(heap, (-count, task))
        
        return time