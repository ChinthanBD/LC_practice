#https://leetcode.com/problems/sort-the-jumbled-numbers/?envType=daily-question&envId=2024-07-24
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def convert_number_according_to_jumbled_system(n):
            n_str = str(n)
            mapped_str = ''.join(str(mapping[int(digit)]) for digit in n_str)
            return int(mapped_str)
            
        return sorted(nums, key=convert_number_according_to_jumbled_system)
