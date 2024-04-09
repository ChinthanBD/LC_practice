# https://leetcode.com/problems/simplify-path/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split the path by '/'
        parts = path.split('/')
        stack = []

        # Process each part of the path
        for part in parts:
            if part == '..':
                # If encountering '..', pop the top directory if the stack is not empty
                if stack:
                    stack.pop()
            elif part and part != '.':
                # If the part is not empty and not '.', add it to the stack
                stack.append(part)

        # Reconstruct the simplified path
        simplified_path = '/' + '/'.join(stack)

        return simplified_path
