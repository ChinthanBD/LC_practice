# https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = ''.join(char.lower() for char in s if char.isalnum())

        # l = 0 
        # r = len(s) -1
		
        # while l<r:
        #     if s[l]!=s[r]:
        #         return False
        #     l +=1
        #     r -=1
        # return True

        s = ''.join(char.lower() for char in s if char.isalnum())
        rev = s[::-1]
        return True if s== rev else False