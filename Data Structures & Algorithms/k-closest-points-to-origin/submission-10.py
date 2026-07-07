class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for p in points:
            x, y = p[0], p[1]
            distance = (x ** 2) + (y ** 2)
            heapq.heappush(minHeap, (distance, x, y))
        
        res = []

        while len(res) != k:
            p = heapq.heappop(minHeap)
            x, y = p[1], p[2]
            res.append([x, y])
        
        return res