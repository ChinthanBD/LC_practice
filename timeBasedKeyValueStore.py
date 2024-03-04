# https://leetcode.com/problems/time-based-key-value-store/description/
from typing import defaultdict
class TimeMap:

    def __init__(self):
        self.mpp = defaultdict(list)  # key = string, value = [string, timestamp]

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


class TimeMap:

    def __init__(self):
        self.mpp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mpp[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mpp:
            return ""
        
        v = ""     
        values_list =  self.mpp.get(key)
        l = 0
        r = len(values_list) -1

        while l<=r:
            mid = (l+r) // 2

            if values_list[mid][1] == timestamp:
                return values_list[mid][0]
            
            elif values_list[mid][1] > timestamp:
                r = mid -1
            
            else:
                v = values_list[mid][0]
                l = mid +1
        
        return v


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)    