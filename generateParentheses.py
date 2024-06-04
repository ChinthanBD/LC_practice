# https://leetcode.com/problems/generate-parentheses/           
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []  # List to store the valid combinations of parentheses

        # Helper function to generate valid sets of parentheses
        def get_valid_set(open_brackets, closing_brackets, pair_gen):
            # Base case: if both open and close brackets have reached 'n', add the generated string to the answer list
            if closing_brackets == n and open_brackets == n:
                ans.append(pair_gen)
                return 
            
            # If the number of open brackets is less than 'n', add an open bracket and recurse
            if open_brackets < n:
                get_valid_set(open_brackets + 1, closing_brackets, pair_gen + '(')
            
            # If the number of closing brackets is less than the number of open brackets, add a closing bracket and recurse
            if closing_brackets < open_brackets:
                get_valid_set(open_brackets, closing_brackets + 1, pair_gen + ')')
        
        # Initialize the recursion with 0 open and close brackets, and an empty string
        get_valid_set(0, 0, "")

        return ans  # Return the list of valid parentheses combinations
