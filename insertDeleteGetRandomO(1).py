# https://leetcode.com/problems/insert-delete-getrandom-o1/
import random

class RandomizedSet:

    def __init__(self):
        self.hashMap = {}
        self.lst = []
        

    def insert(self, val: int) -> bool:
        res = val not in self.hashMap
        if res:
            self.hashMap[val] = len(self.lst)
            self.lst.append(val)
        return res
        

    def remove(self, val: int) -> bool:
        res = val in self.hashMap
        if res:
            idx = self.hashMap[val]
            lastVal = self.lst[-1]
            self.lst[idx] = lastVal
            self.lst.pop()
            self.hashMap[lastVal] = idx
            del self.hashMap[val]
        return res
        

    def getRandom(self) -> int:
        return random.choice(self.lst)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()