# https://leetcode.com/problems/time-based-key-value-store/description/
from typing import defaultdict
class TimeMap:

    def __init__(self):
        self.mpp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mpp[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mpp:
            return ""
        
        v = ""
        for value, timestmp in self.mpp[key]:
            if timestmp == timestamp:
                return value
            elif int(timestmp) < timestamp:
                v = value
        return v
                 


# TLE for above  :(