# https://leetcode.com/problems/find-center-of-star-graph/description/?envType=daily-question&envId=2024-06-27
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        lookup_list = []

        for u,v in edges:
            if u in lookup_list:
                return u
            if v in lookup_list:
                return v
            lookup_list.append(u)
            lookup_list.append(v)