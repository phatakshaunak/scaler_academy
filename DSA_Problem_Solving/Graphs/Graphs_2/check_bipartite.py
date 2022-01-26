'''Q3. Check whether the graph is bipartite or not
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a undirected graph having A nodes. A matrix B of size M x 2 is given which represents the edges such that there is an edge between B[i][0] and B[i][1].

Find whether the given graph is bipartite or not.

A graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B

Note:

There are no self-loops in the graph.

No multiple edges between two pair of vertices.

The graph may or may not be connected.

Nodes are Numbered from 0 to A-1.

Your solution will run on multiple testcases. If you are using global variables make sure to clear them.



Problem Constraints

1 <= A <= 100000

1 <= M <= min(A*(A-1)/2,200000)

0 <= B[i][0],B[i][1] < A



Input Format

The first argument given is an integer A.

The second argument given is the matrix B.



Output Format

Return 1 if the given graph is bipartide else return 0.



Example Input

Input 1:

A = 2
B = [ [0, 1] ]
Input 2:

A = 3
B = [ [0, 1], [0, 2], [1, 2] ]


Example Output

Output 1:

1
Output 2:

0


Example Explanation

Explanation 1:

Put 0 and 1 into 2 different subsets.
Explanation 2:

 
It is impossible to break the graph down to make two different subsets for bipartite matching'''

import sys
sys.setrecursionlimit(int(1e6))

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):

        # Build adjacency list and initialize a color array (0 and 1)
        adj = [[] for i in range(A)]
        col = [-1 for i in range(A)]

        for e in B:
            x, y = e[0], e[1]

            adj[x].append(y)
            adj[y].append(x)

        # Iterate all vertices to cover all connected components. Assign each start node a color of 0
        for i in range(A):

            if col[i] == -1:
                col[i] = 0
                ans = self.dfs_2color(i, adj, col)

                # If ans gets a false, return False
                if ans == False:
                    return 0
                    
                # If ans gets a true, loop through all vertices and return True if loop is complete as another connected component may not satisfy 2-coloring

        return 1
    
    def dfs_2color(self, node, adj, col):

        for nb in adj[node]:

            # If neighbor is colored with the same color as given node, return False
            if col[nb] != -1 and col[nb] == col[node]:
                return False
            
            # If neighbor not colored, assign alternate color
            elif col[nb] == -1:
                col[nb] = col[node] ^ 1
                
                # Collect ans for running a dfs on nb. If it returns False, no need to check further, return False. Else continue dfs
                ans = self.dfs_2color(nb, adj, col)
                if not ans:
                    return False
        
        # If nothing is returned, return True as 2 colors are possible
        return True