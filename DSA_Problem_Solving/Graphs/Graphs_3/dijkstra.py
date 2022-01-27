'''Q2. Dijsktra
Unsolved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a weighted undirected graph having A nodes and M weighted edges, and a source node C.

You have to find an integer array D of size A such that:

=> D[i] : Shortest distance form the C node to node i.

=> If node i is not reachable from C then -1.

Note:

There are no self-loops in the graph.

No multiple edges between two pair of vertices.

The graph may or may not be connected.

Nodes are numbered from 0 to A-1.

Your solution will run on multiple testcases. If you are using global variables make sure to clear them.



Problem Constraints

1 <= A <= 1e5

0 <= B[i][0],B[i][1] < A

0 <= B[i][2] <= 1e3

0 <= C < A



Input Format

The first argument given is an integer A, representing the number of nodes.

The second argument given is the matrix B of size M x 3, where nodes B[i][0] and B[i][1] are connected with an edge of weight B[i][2].

The third argument given is an integer C.



Output Format

Return the integer array D.



Example Input

Input 1:

A = 6
B = [   [0, 4, 9]
        [3, 4, 6] 
        [1, 2, 1] 
        [2, 5, 1] 
        [2, 4, 5] 
        [0, 3, 7] 
        [0, 1, 1] 
        [4, 5, 7] 
        [0, 5, 1] ] 
C = 4
Input 2:

A = 5
B = [   [0, 3, 4]
        [2, 3, 3] 
        [0, 1, 9] 
        [3, 4, 10] 
        [1, 3, 8]  ] 
C = 4


Example Output

Output 1:

D = [7, 6, 5, 6, 0, 6]
Output 2:

D = [14, 18, 13, 10, 0]


Example Explanation

Explanation 1:

 All Paths can be considered from the node C to get shortest path
Explanation 2:

 All Paths can be considered from the node C to get shortest path'''

from heapq import heappush, heappop
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):

        # Create adjacency list, add neighbors along with the weights
        adj = [[] for i in range(A)]

        for e in B:

            u, v, w = e

            adj[u].append([v, w])
            
            adj[v].append([u, w])
        
#         print(adj)
        heap = []

        # Initialize distance array with -1
        ans = [-1 for i in range(A)]

        # Mark source node's distance as 0
        ans[C] = 0

        # Maintain a visited array similar to a BFS/DFS traversal
        vis = [0 for i in range(A)]

        # Maintain a path array to get shortest path
        path = [None for i in range(A)]

        # Push distance first for heapifying along with source node and path from to heap
        heappush(heap, (0, C, -1))

        # Iterate until heap is non empty
        while heap:

            # Pop node
            d, node, p_from = heappop(heap)

            # Add its unvisited neighbors to the heap
            for nb in adj[node]:

                v, w = nb

                if vis[v] != 1:

                    # Push the neighbor as a tuple of distance from source, node name and the node name it came from
                    heappush(heap, (d + w, v, node))
            
            # Here update distance if node has not been visited and then update visit array and path array
            if vis[node] != 1:
                vis[node] = 1
                ans[node] = d
                path[node] = p_from
        
        # Trace path for all nodes
        # for i in range(A):
            
        #     if i != C:
            
        #         path_ = []
        #         idx = path[i]
        #         path_.append(str(i))

        #         while path[idx] != -1:
        #             path_.append(str(idx))
        #             idx = path[idx]
        #         path_.append(str(C))
        #         path_.reverse()

        #         print('Shortest path from source for node', i, ' is: ', '-'.join(path_))
        return ans