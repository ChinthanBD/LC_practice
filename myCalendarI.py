# https://leetcode.com/problems/my-calendar-i/?envType=daily-question&envId=2024-09-26
class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.calendar:
            # Check if the new event overlaps with any existing event
            if start < e and s < end:
                return False
        self.calendar.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
 
