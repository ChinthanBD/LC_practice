#https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/submissions/1408445482/?envType=daily-question&envId=2024-10-01
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # Step 1: Calculate remainders and their frequencies
        remainder_count = [0] * k
        
        for num in arr:
            remainder = num % k
            # Adjust remainder to be positive
            if remainder < 0:
                remainder += k
            remainder_count[remainder] += 1

        # Step 2: Check pairing conditions
        # Check for remainder 0
        if remainder_count[0] % 2 != 0:
            return False
        
        # Check for other remainders
        for r in range(1, k):
            if remainder_count[r] != remainder_count[k - r]:
                return False
        
        return True

