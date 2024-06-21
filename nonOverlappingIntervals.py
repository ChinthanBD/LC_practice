# https://leetcode.com/problems/non-overlapping-intervals/description/
from typing import List 

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals based on their end times
        intervals.sort(key=lambda x: x[1])
        
        # Initialize the count of intervals to remove
        remove_count = 0
        # Initialize the end time of the last added interval
        end_time = float('-inf')
        
        for interval in intervals:
            if interval[0] < end_time:
                # There is an overlap, increment the removal count
                remove_count += 1
            else:
                # No overlap, update the end time to the current interval's end time
                end_time = interval[1]
        
        return remove_count
