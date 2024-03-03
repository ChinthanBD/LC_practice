# https://leetcode.com/problems/combination-sum/
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        container = [] # to store the individual combination
        ans = [] # answer array to store all the combinations
        def combination(target_value, index, container):
            if target_value == 0:
                ans.append(container.copy())
                return
            if index >= len(candidates) or target_value < 0:  # Added condition to handle out of bounds and negative target_value
                return  

            if candidates[index] <= target:
                container.append(candidates[index])
                combination(target_value - candidates[index], index, container)
                container.pop()
            
            combination(target_value , index +1, container)
        
        combination(target, 0, container)

        return ans

                
        