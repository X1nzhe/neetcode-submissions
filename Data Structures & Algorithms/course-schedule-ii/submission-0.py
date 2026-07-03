class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_pre_map = defaultdict(list)
        for c, p in prerequisites:
            course_pre_map[c].append(p)
        
        res = []
        visiting = set()
        visited = set()
        
        def dfs(course):
            if course in visiting: # found cycle
                return False
            if course in visited:
                return True
            visiting.add(course)
            for p in course_pre_map[course]:
                if not dfs(p):
                    return False
            visiting.remove(course)

            visited.add(course)
            res.append(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return res
        