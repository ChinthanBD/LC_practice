# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/?envType=daily-question&envId=2024-07-11
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for char in s:
            if char in ")":
                substring = []
                while stack and stack[-1] != '(':
                    substring.append(stack.pop())
                stack.pop()  # pop the '('
                stack.extend(substring)
            else:
                stack.append(char) 
            
        return ''.join(stack)
