'''Q5. Topological Sort
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an directed acyclic graph having A nodes. A matrix B of size M x 2 is given which represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge uv, vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.

Return the topological ordering of the graph and if it doesn't exist then return an empty array.

If there is a solution return the correct ordering. If there are multiple solutions print the lexographically smallest one.

Ordering (a, b, c) is said to be lexographically smaller than ordering (e, f, g) if a < e or if(a==e) then b < f and so on.

NOTE:

There are no self-loops in the graph.
There are no multiple edges between two nodes.
The graph may or may not be connected.
Nodes are numbered from 1 to A.
Your solution will run on multiple test cases. If you are using global variables make sure to clear them.


Problem Constraints

2 <= A <= 104

1 <= M <= min(100000,A*(A-1))

1 <= B[i][0], B[i][1] <= A



Input Format

The first argument given is an integer A representing the number of nodes in the graph.

The second argument given a matrix B of size M x 2 which represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].



Output Format

Return a one-dimensional array denoting the topological ordering of the graph and it it doesn't exist then return empty array.



Example Input

Input 1:

 A = 6
 B = [  [6, 3] 
        [6, 1] 
        [5, 1] 
        [5, 2] 
        [3, 4] 
        [4, 2] ]
Input 2:

 A = 3
 B = [  [1, 2]
        [2, 3] 
        [3, 1] ]


Example Output

Output 1:

 [5, 6, 1, 3, 4, 2]
Output 2:

 []


Example Explanation

Explanation 1:

 The given graph contain no cycle so topological ordering exists which is [5, 6, 1, 3, 4, 2]
Explanation 2:

 The given graph contain cycle so topological ordering not possible we will return empty array.'''

import heapq
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):

        # Initialize arrays for adjacency list, in degrees, min heap ans ans array
        min_heap, ans = [], []
        adj, in_ = [[] for i in range(A + 1)], [0 for i in range(A + 1)]

        # Build adjacency list and in degree array
        for e in B:
            x, y = e[0], e[1]

            adj[x].append(y)
            in_[y] += 1
        
        # Find all zero degree nodes and add to min heap to maintain lexicographical order
        for i in range(A + 1):
            if i != 0 and in_[i] == 0:
                heapq.heappush(min_heap, i)
        
        # Iterate over min_heap until it is non empty
        while min_heap:

            # Get smallest zero degree node
            top = heapq.heappop(min_heap)

            # Add to ans for topological sorted order
            ans.append(top)

            # Subtract all of top's out degrees iterating its adjacency list
            for nb in adj[top]:
                in_[nb] -= 1

                # If in degrees become zero, add to min heap
                if in_[nb] == 0:
                    heapq.heappush(min_heap, nb)
        
        # If graph is cyclic, topological sort is not possible, here len(ans) would not be equal to A, in that case return empty list
        if len(ans) != A:

            while ans: ans.pop()
            return ans
        
        return ans
    
    # TC: O(VlogV + E), SC: O(V + E)