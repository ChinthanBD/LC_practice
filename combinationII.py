# https://leetcode.com/problems/combination-sum-ii/
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Sort candidates to handle duplicates
        ans = []  # answer array to store all the combinations

        def combination(target_value, index, container):
            if target_value == 0:
                ans.append(container[:])  # Append a copy of container to ans
                return

            for i in range(index, len(candidates)):
                # Skip duplicates
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                # Check if the current candidate can be included
                if candidates[i] <= target_value:
                    container.append(candidates[i])
                    combination(target_value - candidates[i], i + 1, container)
                    container.pop()

        combination(target, 0, [])
        return ans



class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Sort candidates to handle duplicates

        ans = []
        def dfs(i, curr_sum, ele_list):
            if curr_sum == target:
                ans.append(ele_list.copy())
                return
            
            if (curr_sum > target or i >= len(candidates)):
                return 
            
            # include current index and call for next index
            ele_list.append(candidates[i])
            dfs(i+1, curr_sum + candidates[i], ele_list)
            ele_list.pop()

            # exclude current index, skip duplicates and call for next index
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            
            dfs(i+1, curr_sum, ele_list)

        
        dfs(0, 0, [])

        return ans

