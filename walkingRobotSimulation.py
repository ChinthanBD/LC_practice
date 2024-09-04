# https://leetcode.com/problems/walking-robot-simulation/submissions/1379110539/?envType=daily-question&envId=2024-09-04
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Directions are represented as vectors (dx, dy)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # North, East, South, West
        direction_index = 0  # Start facing North
        
        x, y = 0, 0  # Starting position
        max_distance_sq = 0  # Maximum distance squared
        
        # Convert obstacle list to a set of tuples for O(1) lookups
        obstacle_set = set(map(tuple, obstacles))
        
        for command in commands:
            if command == -2:  # Turn left
                direction_index = (direction_index - 1) % 4
            elif command == -1:  # Turn right
                direction_index = (direction_index + 1) % 4
            else:  # Move forward
                dx, dy = directions[direction_index]
                for _ in range(command):
                    # Check if the next position is an obstacle
                    if (x + dx, y + dy) not in obstacle_set:
                        x += dx
                        y += dy
                        # Update the maximum distance squared
                        max_distance_sq = max(max_distance_sq, x*x + y*y)
                    else:
                        break  # Stop moving if there's an obstacle
            
        return max_distance_sq
