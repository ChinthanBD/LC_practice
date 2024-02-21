# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = haystack.find(needle)

        return res



##############
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        for i in range(len(haystack) +1):
            if haystack[i:i + len(needle)] == needle:
                return i
        
        return -1