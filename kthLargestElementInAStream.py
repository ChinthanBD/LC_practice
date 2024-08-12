# https://leetcode.com/problems/kth-largest-element-in-a-stream/?envType=daily-question&envId=2024-08-12
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        
        # Add each number in nums to the heap
        for num in nums:
            self.add(num)
    
    def add(self, val: int) -> int:
        # Add the new value to the heap
        heapq.heappush(self.min_heap, val)
        
        # If the heap exceeds size k, remove the smallest element
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        # The root of the heap is the k-th largest element
        return self.min_heap[0]     


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
