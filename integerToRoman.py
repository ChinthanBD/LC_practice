# https://leetcode.com/problems/integer-to-roman/?envType=study-plan-v2&envId=top-interview-150
# class Solution:
#     def intToRoman(self, num: int) -> str:
#         symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
#         values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#         result = ""
#         for i in range(len(values)):
#             while num >= values[i]:
#                 result += symbols[i]
#                 num -= values[i]
#         return result

class Solution:
    def intToRoman(self, num: int) -> str:
        symbol_values = {
            "M": 1000, "CM": 900, "D": 500, "CD": 400,
            "C": 100, "XC": 90, "L": 50, "XL": 40,
            "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1
        }

        result = ""
        for symbol, value in symbol_values.items():
            while num >= value:
                result += symbol
                num -= value

        return result