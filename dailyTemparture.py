# https://leetcode.com/problems/daily-temperatures/description/
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        next_greater_element = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)-1, -1, -1):
            while next_greater_element and temperatures[next_greater_element[-1]] <= temperatures[i]:
                next_greater_element.pop()

            if next_greater_element:
                res[i] = next_greater_element[-1] - i
            
            next_greater_element.append(i)
        return res

        