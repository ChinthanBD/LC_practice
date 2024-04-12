# https://leetcode.com/problems/evaluate-reverse-polish-notation/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                stack.append(int(token))
            else:
                second_operand = stack.pop()
                first_operand = stack.pop()
                if token == '+':
                    result = first_operand + second_operand
                elif token == '-':
                    result = first_operand - second_operand
                elif token == '*':
                    result = first_operand * second_operand
                elif token == '/':
                    # Ensure integer division (truncates toward zero)
                    result = int(first_operand / second_operand)
                stack.append(result)
        return stack.pop()
