# https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/?envType=daily-question&envId=2024-07-08
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def get_index(curr_index, steps, length):
            # Adjust steps to be within the length of the list
            new_index = (curr_index + steps - 1) % length
            return new_index
        
        def get_res(arr, index):
            if len(arr) == 1:
                return arr[0]
            
            index = get_index(index, k, len(arr))
            arr.pop(index)
            return get_res(arr, index)
        
        return get_res([i for i in range(1, n + 1)], 0)

