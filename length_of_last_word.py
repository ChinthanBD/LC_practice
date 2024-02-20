# https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = len(s.split()[-1])
        return res