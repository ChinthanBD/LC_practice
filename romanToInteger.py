# https://leetcode.com/problems/roman-to-integer/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        if len(s) == 1:
            return roman_to_int[s]

        for i in range(0, len(s)-1):
            if roman_to_int[s[i]] <roman_to_int[s[i+1]]:
                sum -= roman_to_int[s[i]]
            else:
                sum += roman_to_int[s[i]]
        sum+= roman_to_int[s[-1]]

        return sum
            
