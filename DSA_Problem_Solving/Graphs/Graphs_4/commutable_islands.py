'''Q3. Commutable Islands
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

There are A islands and there are M bridges connecting them. Each bridge has some cost attached to it.

We need to find bridges with minimal cost such that all islands are connected.

It is guaranteed that input data will contain at least one possible scenario in which all islands are connected with each other.



Problem Constraints

1 <= A, M <= 6*104

1 <= B[i][0], B[i][1] <= A

1 <= B[i][2] <= 103



Input Format

The first argument contains an integer, A, representing the number of islands.

The second argument contains an 2-d integer matrix, B, of size M x 3 where Island B[i][0] and B[i][1] are connected using a bridge of cost B[i][2].



Output Format

Return an integer representing the minimal cost required.



Example Input

Input 1:

 A = 4
 B = [  [1, 2, 1]
        [2, 3, 4]
        [1, 4, 3]
        [4, 3, 2]
        [1, 3, 10]  ]
Input 2:

 A = 4
 B = [  [1, 2, 1]
        [2, 3, 2]
        [3, 4, 4]
        [1, 4, 3]   ]


Example Output

Output 1:

 6
Output 2:

 6


Example Explanation

Explanation 1:

 We can choose bridges (1, 2, 1), (1, 4, 3) and (4, 3, 2), where the total cost incurred will be (1 + 3 + 2) = 6.
Explanation 2:

 We can choose bridges (1, 2, 1), (2, 3, 2) and (1, 4, 3), where the total cost incurred will be (1 + 2 + 3) = 6.'''

from heapq import heappush, heappop
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):

        # Adjacency list creation needed for Prims not for Kruskal's
        # adj = [[] for i in range(A + 1)]

        # for e in B:

        #     u, v, w = e

        #     # Add edges and weights
        #     adj[u].append((v, w))
        #     adj[v].append((u, w))

        # To run Kruskal's Algorithm, initialize A disjoint sets with a parent array element pointing to the element itself and height array with each element of height 1
        parent = [i for i in range(A + 1)]

        height = [1 for i in range(A + 1)]
        
        # Initially sort all edges on weight in ascending order
        B.sort(key = lambda x: x[2])
        
        # Iterate all edges, run a union function on both nodes. If union is possible, add their weights. Else skip as that indicates the edge is forming a cycle
        ans = 0

        for e in B:
            
            u, v, w = e

            if self.union(u, v, parent, height):
                ans += w
        
        return ans
            
        # return self.prims(A, adj)
    
    def find(self, node, parent):

        if node == parent[node]:
            return node
        
        parent[node] = self.find(parent[node], parent)

        # Path compression, return the found parent for all intermediate nodes
        return parent[node]
    
    def union(self, u, v, parent, height):

        u = self.find(u, parent)

        v = self.find(v, parent)

        if u == v:
            # They both belong to the same disjoint set, no need to do a union
            return False
        
        # If heights are unequal, make node with higher height parent of the other, height remains the same
        if height[u] > height[v]:
            parent[v] = u
        
        elif height[v] > height[u]:
            parent[u] = v
        
        else:
            # If equal heights, make either node as the parent and increment its height by 1
            parent[v] = u
            height[u] += 1
        
        # Since union is possible return True
        return True

    def prims(self, N, adj):
        
        # Initialize a variable to store MST weight sum
        ans = 0

        # Create a visited array and min heap with source node outgoing edges
        vis = [0 for i in range(N + 1)]
        mh = []
        # Choose a start node, say 1 and mark as visited
        u = 1
        vis[u] = 1
        # Add its outgoing edges to min heap
        for nb in adj[u]:

            # Can check if edges are visited, does not matter at this point as all are going to be unvisited
            v, w = nb

            # Push weight first to sort min heap on it
            heappush(mh, (w, u, v))

        # Loop until min heap is not empty
        while mh:

            # Pop the min
            w, u, v = heappop(mh)

            # If v is unvisited, add the edge weight to ans and then add its unvisited neighbor edges to the heap
            if vis[v] != 1:

                # Add edge weight to ans and mark visited
                ans += w
                vis[v] = 1

                # Add unvisited neighbor edges
                for nb in adj[v]:

                    n, w = nb

                    if vis[n] != 1:
                        heappush(mh, (w, v, n))
        
        return ans