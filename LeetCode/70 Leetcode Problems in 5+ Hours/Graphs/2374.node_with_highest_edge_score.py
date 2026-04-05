class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        
        # Will have to traverse all the edges because some might be in isolation

        # The position indicates what each node points to + its number (@ i = 1, val = 0, so the Node(val = 1, neighbors = [0]))

        # Traverse all the nodes
        # Then use a mapping { idx : edge_score }
        edge_map = {}
        for idx, point in enumerate(edges):
            if (point not in edge_map.keys()):
                edge_map[point] = idx
            else:
                edge_map[point] += idx

        max_edge_score = max(edge_map.values())
        vals = [idx for idx, edge_score in edge_map.items() if edge_score == max_edge_score]
        return min(vals)