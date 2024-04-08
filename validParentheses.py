# https://leetcode.com/problems/valid-parentheses/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        mpp = {')':'(','}':'{',']':'['}
        
        for bracket in s:
            if bracket in mpp:
                if not stk or stk.pop() != mpp[bracket]:
                    return False
            else:
                stk.append(bracket)
                
        return not stk
