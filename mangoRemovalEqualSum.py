# Sharpsell

# You are given an array of integers, weights where each integer in the array represents the weight of a mango. 
# You have to find the number of ways in which one mango can be removed from the list, 
# such that the sum of weights of the mangoes at the even positions and the sum of weights of mangoes at the odd positions in the resulting list, are equal

def count_valid_removals(weights):
    n = len(weights)
    if n == 0:
        return 0
    
    even_sum = 0
    odd_sum = 0
    
    # Compute initial sums for even and odd indices
    for i in range(n):
        if i % 2 == 0:
            even_sum += weights[i]
        else:
            odd_sum += weights[i]
    
    valid_removals = 0
    
    current_even_sum = 0
    current_odd_sum = 0
    
    for i in range(n):
        if i % 2 == 0:
            even_sum -= weights[i]
        else:
            odd_sum -= weights[i]
        
        if current_even_sum + odd_sum == current_odd_sum + even_sum:
            valid_removals += 1
        
        if i % 2 == 0:
            current_even_sum += weights[i]
        else:
            current_odd_sum += weights[i]
    
    return valid_removals

# Example usage:
weights = [1, 2, 3, 4, 5, 6]
print(count_valid_removals(weights))  # Output the number of valid removals
