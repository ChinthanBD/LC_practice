# https://leetcode.com/problems/the-dining-philosophers/description/
from typing import Callable
from threading import Lock

class DiningPhilosophers:
    def __init__(self):
        self.locks = [Lock() for _ in range(5)]

    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        left = philosopher
        right = (philosopher + 1) % 5
        
        # Ensure philosophers with odd ids pick up right fork first to prevent deadlock
        if philosopher % 2 == 1:
            self.locks[left].acquire()
            self.locks[right].acquire()
        else:
            self.locks[right].acquire()
            self.locks[left].acquire()
        
        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()
        
        self.locks[left].release()
        self.locks[right].release()
