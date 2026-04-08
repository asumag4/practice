from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        courses = defaultdict(list)
        for course, prereq in prerequisites:
            courses[course].append(prereq)

        taken = set()

        def findPrereq(course):
            # print(course, courses) # DEBUG

            if not courses[course]: # Then there's no prereq
                return True
            
            if course in taken: # Then theres circular dependency
                return False

            taken.add(course)

            for prereq in courses[course]:
                if not findPrereq(prereq): return False

            courses[course] = [] 

            return True # Default case

        for course, _ in prerequisites:
            if not findPrereq(course): return False

        return True