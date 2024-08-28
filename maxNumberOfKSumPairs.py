# https://leetcode.com/problems/max-number-of-k-sum-pairs/submissions/1371238159/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Initialize a dictionary to count the frequency of each number
        count = defaultdict(int)
        operations = 0
        
        for num in nums:
            complement = k - num
            # Check if the complement exists in the dictionary
            if count[complement] > 0:
                # A pair is found, so we decrement the count of the complement
                count[complement] -= 1
                operations += 1
            else:
                # No complement found, increment the count of the current number
                count[num] += 1
        
        return operations
