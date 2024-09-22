# https://leetcode.com/problems/asteroid-collision/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        ans = []
        
        for asteroid in asteroids:
            # Handle collisions
            while ans and asteroid < 0 < ans[-1]:
                # If the moving right asteroid (ans[-1]) is smaller, it explodes
                if ans[-1] < -asteroid:
                    ans.pop()
                    continue
                # If the asteroids are equal size, both explode
                elif ans[-1] == -asteroid:
                    ans.pop()
                break
            else:
                # No collision or collision results in current asteroid surviving
                ans.append(asteroid)
        
        return ans
