# https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if not x:
            return True
        s = str(x)
        return s == s[::-1]        