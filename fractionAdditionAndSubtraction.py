# https://leetcode.com/problems/fraction-addition-and-subtraction/?envType=daily-question&envId=2024-08-23
from fractions import Fraction
import re
class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Find all fractions in the expression
        fractions = re.findall('[+-]?\d+/\d+', expression)
        
        # Initialize the result as a Fraction object
        result = sum(Fraction(frac) for frac in fractions)
        
        # Convert the result to an irreducible fraction
        numerator = result.numerator
        denominator = result.denominator
        
        # Return the fraction as a string
        return f"{numerator}/{denominator}"
