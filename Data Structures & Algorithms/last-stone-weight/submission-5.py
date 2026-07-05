import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        for n in stones:
            heapq.heappush(maxHeap, -n)

        while len(maxHeap) >= 2:
            y = -heapq.heappop(maxHeap)  # use minus to get back positive number
            x = -heapq.heappop(maxHeap)
            if x < y:
                y = y - x
                heapq.heappush(maxHeap, -y)
        
        
        return -maxHeap[0] if maxHeap else 0

