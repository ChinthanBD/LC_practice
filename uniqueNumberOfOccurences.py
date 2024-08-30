# https://leetcode.com/problems/unique-number-of-occurrences/submissions/1373010659/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_map = {}
        for num in arr:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1
        
        # Step 2: Check if the counts are unique
        counts = list(count_map.values())
        return len(counts) == len(set(counts))
