# Last updated: 7/9/2026, 9:45:25 PM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_Heap = [-num for num in nums]
        heapq.heapify(max_Heap)
        for i in range(k-1):
            heapq.heappop(max_Heap)
        
        return -heapq.heappop(max_Heap)