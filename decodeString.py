# https://leetcode.com/problems/decode-string/submissions/1401889292/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def decodeString(self, s: str) -> str:
        # Stack for storing numbers and strings
        num_stack = []
        str_stack = []
        current_str = ''
        current_num = 0

        # Iterate through each character in the string
        for char in s:
            if char.isdigit():
                # Build the number for k (can be multiple digits)
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push the current number and string to their stacks
                num_stack.append(current_num)
                str_stack.append(current_str)
                # Reset for the new block inside []
                current_str = ''
                current_num = 0
            elif char == ']':
                # Pop from stack and repeat the string accordingly
                repeat_num = num_stack.pop()
                prev_str = str_stack.pop()
                current_str = prev_str + current_str * repeat_num
            else:
                # Accumulate the current characters
                current_str += char

        return current_str
