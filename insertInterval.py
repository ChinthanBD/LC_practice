# https://leetcode.com/problems/insert-interval/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        start, end = newInterval
        
        for curr_start,curr_end in intervals:
            # If current interval ends before the new interval starts, add it directly to the result
            if curr_end < start:
                merged.append([curr_start, curr_end])
            # If current interval starts after the new interval ends, add the new interval and then add the current interval
            elif curr_start > end:
                merged.append([start, end])
                start, end = curr_start, curr_end
            # If there's an overlap, merge the intervals by updating the new interval
            else:
                start = min(start, curr_start)
                end = max(end, curr_end)
        
        merged.append([start, end])  # Add the remaining new interval
        return merged
