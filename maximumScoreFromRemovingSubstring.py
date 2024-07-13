# https://leetcode.com/problems/maximum-score-from-removing-substrings/?envType=daily-question&envId=2024-07-12
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pairs(s, first, second, value):
            count = 0
            stack = []
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    count += value
                else:
                    stack.append(char)
            return ''.join(stack), count

        # Determine which pair to remove first based on values of x and y
        if x > y:
            s, gain_x = remove_pairs(s, 'a', 'b', x)
            s, gain_y = remove_pairs(s, 'b', 'a', y)
        else:
            s, gain_y = remove_pairs(s, 'b', 'a', y)
            s, gain_x = remove_pairs(s, 'a', 'b', x)

        return gain_x + gain_y