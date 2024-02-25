# https://leetcode.com/problems/merge-intervals/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort()  # Sort the intervals based on start times
        output = []
        start, end = intervals[0]  # Initialize start and end
        
        for interval in intervals[1:]:
            if interval[0] <= end:
                end = max(end, interval[1])  # Merge overlapping intervals
            else:
                output.append([start, end])  # Add non-overlapping interval to output
                start, end = interval  # Update start and end for the new interval
        
        output.append([start, end])  # Append the last interval
        return output