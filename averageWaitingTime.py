# https://leetcode.com/problems/average-waiting-time/description/?envType=daily-question&envId=2024-07-09
from typing import List
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_time = 0
        finish_time = 0

        for arrivali, cooking_time in customers:
            if arrivali > finish_time:
                # If the arrival time is after the finish time, the chef is idle until the customer arrives
                finish_time = arrivali
            
            # Update finish time by adding the cooking time
            finish_time += cooking_time
            # Wait time is the time from arrival to finish
            wait_time = finish_time - arrivali
            total_time += wait_time
        
        # Return the average waiting time
        return total_time / len(customers)
