# https://leetcode.com/problems/plus-one/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Start from the least significant digit
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                # If the current digit is less than 9, simply add one and return
                digits[i] += 1
                return digits
            else:
                # If the current digit is 9, set it to 0 and continue with the next significant digit
                digits[i] = 0
        
        # If all digits were 9, insert 1 at the beginning
        return [1] + digits
