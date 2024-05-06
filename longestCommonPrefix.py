# https://leetcode.com/problems/longest-common-prefix/?envType=study-plan-v2&envId=top-interview-150
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # prefix = strs[0]

        # for s in strs[1:]:
        #     while s.find(prefix) != 0:
        #         prefix = prefix[:-1]

        #     if not prefix:
        #         return ""
        # return prefix

        ###################
        # res = ''
        # for i in range(len(strs[0])):
        #     for s in strs[1:]:
        #         if i == len(s) or s[i]!= strs[0][i]:
        #             return res
                
        #     res+= strs[0][i]
        # return res

        #################
        if len(strs) ==1 or not strs:
            return strs[0]

        min_str, max_str = min(strs), max(strs)
        for i in range(len(min_str)):
            if min_str[i] != max_str[i]:
                return min_str[:i]
        return min_str