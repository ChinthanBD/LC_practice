# https://leetcode.com/problems/gas-station/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        total = 0
        start =0 
        for i in range(len(cost)):
            total += gas[i] - cost[i]

            if total<0:
                total = 0
                start = i+1
        return start

        ###### TILE For below
        # n = len(gas)
        # for i in range(n):
        #     gas_current = gas[i]
        #     j = i
        #     while gas_current >= cost[j]:
        #         gas_current -= cost[j]
        #         j = (j+1)%n
        #         if i == j: 
        #             return i
        #         gas_current += gas[j]
        # return -1


