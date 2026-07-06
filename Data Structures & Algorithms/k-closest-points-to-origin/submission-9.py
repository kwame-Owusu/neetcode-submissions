import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for p in points:
            x = p[0]
            y = p[1]
            distance = (x ** 2) + (y ** 2)
            pair = (distance, x, y)

            minHeap.append(pair)
        
        heapq.heapify(minHeap)

        res = []

        while len(res) != k:
            p = heapq.heappop(minHeap) # points (distance, x, y)
            res.append([p[1], p[2]])
            
        return res