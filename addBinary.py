# https://leetcode.com/problems/add-binary/description/?envType=study-plan-v2&envId=top-interview-150
from typing import str
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ""
        # Starting from the rightmost digit
        i, j = len(a) - 1, len(b) - 1
        
        # While there are digits left in either string or carry is not zero
        while i >= 0 or j >= 0 or carry:
            sum_val = carry
            
            if i >= 0:
                sum_val += int(a[i])
                i -= 1
            if j >= 0:
                sum_val += int(b[j])
                j -= 1
            
            # Append the result
            result = str(sum_val % 2) + result
            # Calculate carry for the next iteration
            carry = sum_val // 2
        
        return result
