# https://leetcode.com/problems/permutations/description/
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def generate_perm(container, permutation):
            if len(container) == 0:
                ans.append(permutation[:])  # Append a copy of the permutation list
                return 

            for i in range(len(container)):
                # Create a new list for the current permutation
                new_permutation = permutation + [container[i]]
                generate_perm(container[:i] + container[i+1:], new_permutation)
        
        generate_perm(nums, [])
        return ans


# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         def generate_permutations(start):
#             if start == len(nums):
#                 ans.append(nums[:])  # Append a copy of the current state
#                 return

#             for i in range(start, len(nums)):
#                 # Swap elements to generate permutations in-place
#                 nums[start], nums[i] = nums[i], nums[start]
#                 generate_permutations(start + 1)
#                 # Backtrack by swapping elements back to the original state
#                 nums[start], nums[i] = nums[i], nums[start]

#         ans = []
#         generate_permutations(0)
#         return ans