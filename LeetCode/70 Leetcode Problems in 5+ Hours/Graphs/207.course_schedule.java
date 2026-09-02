import java.util.*;

class Solution {

    private boolean colour_helper(List<List<Integer>> graph, int[] colour, int k) {
        colour[k] = 1;
        for (int edge: graph.get(k)) {
            if (colour[edge] == 1) {
                return true;
            } else if (colour[edge] == 0) {
                if (this.colour_helper(graph, colour, edge)) {
                    return true;
                }
            }
        }

        colour[k] = 2;
        return false;
    }

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>(numCourses);
        int[] colour = new int[numCourses];

        for (int i=0; i<numCourses; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] req: prerequisites) {
            int u = req[0];
            int v = req[1];
            graph.get(u).add(v);
        }

        for (int i=0; i<numCourses; i++) {
            if (this.colour_helper(graph, colour, i)) {
                return false;
            }
        }

        return true;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][] test1 = {{1,4},{2,4},{3,1},{3,2}};
        System.out.println("Test 1 (numCourses=5, prerequisites=" + Arrays.deepToString(test1) + ") => " + sol.canFinish(5, test1));
    }
}