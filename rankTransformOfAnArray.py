# https://leetcode.com/problems/rank-transform-of-an-array/?envType=daily-question&envId=2024-10-02
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Step 1: Sort unique elements
        sorted_unique = sorted(set(arr))
        
        # Step 2: Create a dictionary that maps each element to its rank
        rank_map = {val: idx + 1 for idx, val in enumerate(sorted_unique)}
        
        # Step 3: Replace each element in the original array with its rank
        return [rank_map[val] for val in arr]
