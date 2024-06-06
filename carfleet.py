# https://leetcode.com/problems/car-fleet/
from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        next_greater_arrival_time = []

        cars = [(pos, spd) for pos, spd in zip(position,speed)]
        cars = sorted(cars, key=lambda x: x[0])

        for i in range(len(cars)-1, -1, -1):

            time_for_curr_car = (target - cars[i][0]) / cars[i][1]
            if not next_greater_arrival_time or next_greater_arrival_time[-1] < time_for_curr_car:
                next_greater_arrival_time.append(time_for_curr_car)

        return len(next_greater_arrival_time)