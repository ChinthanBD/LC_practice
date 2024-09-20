# https://leetcode.com/problems/removing-stars-from-a-string/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def removeStars(self, s: str) -> str:
        lst = []
        for letter in s:
            if letter == '*':
                lst.pop()
            else:
                lst.append(letter)
    
        return ''.join(lst)
