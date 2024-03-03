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