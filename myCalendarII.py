# https://leetcode.com/problems/my-calendar-ii/submissions/1404122107/?envType=daily-question&envId=2024-09-27
class MyCalendarTwo:

    def __init__(self):
        self.overlapping_intervals = []
        self.non_overlapping_intervals = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlapping_intervals:
            if end > s and e > start:
                return False
        
        for s, e in self.non_overlapping_intervals:
            if end > s and e > start:
                self.overlapping_intervals.append(
                    (max(s,start), min(e, end))
                )
        self.non_overlapping_intervals.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
