# https://leetcode.com/problems/time-needed-to-buy-tickets/description/

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        q = deque()
        # Build a queue of (ticketsNeeded, originalIndex)
        for i, t in enumerate(tickets):
            q.append((t, i))
        
        time = 0
        while q:
            curr_tickets, curr_idx = q.popleft()
            time += 1  # current person buys 1 ticket
            curr_tickets -= 1
            
            # If this person still needs more tickets, go to the back
            if curr_tickets > 0:
                q.append((curr_tickets, curr_idx))
            
            # If that person was k AND they are done, we can stop
            if curr_idx == k and curr_tickets == 0:
                return time
        
        return time
