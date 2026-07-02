class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses_map = defaultdict(list)
        for c, p in prerequisites:
            courses_map[c].append(p)
        

        def dfs(course, visiting):
            if course in visiting:
                return False
            if courses_map[course] == []:
                return True
            visiting.add(course)
            for pre in courses_map[course]:
                if not dfs(pre, visiting):
                    return False
            visiting.remove(course)
            courses_map[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c, set()):
                return False
        return True
        