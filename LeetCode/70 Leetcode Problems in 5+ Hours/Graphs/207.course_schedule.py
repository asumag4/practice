from collections import deque, defaultdict

class Solution:

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        # Create a graph to represent the courses and their prerequisites

        # use a defaultdict -> if a key is not present, then it will insert the key permanently
        # initialize the defaultdict()
        adj = defaultdict(list)
        # initialize an empty list of courses, with 0 as a positional value
        in_degree = [0] * numCourses

        # Build adjacency list and calculate in-degrees
        # for each course and prereq
        for course, prereq in prerequisites:
            # add the course to the prereq position in the graph
            
            # increment the in-degree of the course

        # Enque all courses with no prerequisites
        # use a deque to queue up all the courses with no prerequisites
        # initialize a counter for all the processed courses

        # while the queue is not empty
            # hold to the leftmost course in the queue
            # increment the counter

            # for each neighbour stored in the graph 
                # decrement the in-degree of the neighbour
                # if the in-degree is 0
                    # set it to the queue 

        # if the processed courses is equal to the number of courses, then return True
        
