# https://leetcode.com/problems/course-schedule-iv/
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)

        for prereq, course in prerequisites:
            adj[course].append(prereq)
        
        prereqMap = {} # (course, prereqs)

        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for neighbour in adj[crs]:
                    prereqMap[crs] |= dfs(neighbour)
                prereqMap[crs].add(crs)
            return prereqMap[crs]
        
        for crs in range(numCourses):
            dfs(crs)

        res = []
        for prereq, course in queries:
            res.append(prereq in prereqMap[course])
        
        return res
                
        



    
