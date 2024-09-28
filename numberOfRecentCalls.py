# https://leetcode.com/problems/number-of-recent-calls/?envType=study-plan-v2&envId=leetcode-75
class RecentCounter:

    def __init__(self):
        # Use deque for efficient popleft operation
        self.requests = deque()
        
    def ping(self, t: int) -> int:
        # Add the new request timestamp to the deque
        self.requests.append(t)
        
        # Remove all requests that are older than t - 3000
        while self.requests[0] < t - 3000:
            self.requests.popleft()
        
        # The length of the deque represents the number of requests in the past 3000 ms
        return len(self.requests)
