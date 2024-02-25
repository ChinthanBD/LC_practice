# https://leetcode.com/problems/longest-common-prefix/?envType=study-plan-v2&envId=top-interview-150
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for s in strs[1:]:
            while s.find(prefix) != 0:
                prefix = prefix[:-1]

            if not prefix:
                return ""
        return prefix