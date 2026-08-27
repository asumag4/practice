class Solution:

    def colour_helper(self, graph: list, colour: list, k: int) -> bool:
        colour[k] = 1
        for edge in graph[k]:
            if colour[edge] == 1:
                return True
            elif colour[edge] == 0:
                    if self.colour_helper(graph, colour, edge):
                        return True

        colour[k] = 2
        return False


    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[u].append(v)

        colour = [0] * numCourses
        for i in range(numCourses):
            if self.colour_helper(graph, colour, i):
                return False

        return True

        
