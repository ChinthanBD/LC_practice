# https://leetcode.com/problems/sort-the-people/?envType=daily-question&envId=2024-07-22
from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # height_name_map = list(zip(heights, names))
        # height_name_map.sort(key =lambda x:x[0], reverse=True)
        # return [name for height, name in height_name_map]
        return [name for _, name in sorted(zip(heights, names), reverse=True)]