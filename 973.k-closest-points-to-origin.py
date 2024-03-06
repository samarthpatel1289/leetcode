class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x,y in points:
            distance = pow(x,2) + pow(y,2) 
            minHeap.append((distance, [x,y]))
        heapq.heapify(minHeap) # O(N)

        return [heapq.heappop(minHeap)[1] for _ in range(k)]