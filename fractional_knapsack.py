# https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1
class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        # function to get maximum value
        arr.sort(key=lambda x: x.value / x.weight, reverse=True)
        total_value = 0
        current_weight = 0
        for item in arr:
            if current_weight + item.weight <= W:
                total_value += item.value
                current_weight += item.weight
            else:
                remaining_capacity = W - current_weight
                total_value += (item.value / item.weight) * remaining_capacity
                break
        return total_value
