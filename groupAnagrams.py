# https://leetcode.com/problems/group-anagrams/description/
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagram_dict = defaultdict(list)

        for s in strs:
            
            sorted_string = ''.join(sorted(s))
            print(sorted_string)
            anagram_dict[sorted_string].append(s)

        for string_list in anagram_dict.values():
            res.append(string_list)

        
        return res
