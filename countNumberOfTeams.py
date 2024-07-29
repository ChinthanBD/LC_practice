from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0

        # Iterate through each soldier to consider it as the middle soldier
        for j in range(n):
            left_smaller, left_greater = 0, 0
            right_smaller, right_greater = 0, 0

            # Count soldiers to the left of j
            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                elif rating[i] > rating[j]:
                    left_greater += 1
            
            # Count soldiers to the right of j
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    right_smaller += 1
                elif rating[k] > rating[j]:
                    right_greater += 1

            # Calculate the number of valid teams with rating[j] as the middle soldier
            count += left_smaller * right_greater + left_greater * right_smaller

        return count
