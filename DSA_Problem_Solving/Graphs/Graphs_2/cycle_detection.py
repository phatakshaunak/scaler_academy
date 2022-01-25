'''Q1. Cycle in Directed Graph
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an directed graph having A nodes. A matrix B of size M x 2 is given which represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].

Find whether the graph contains a cycle or not, return 1 if cycle is present else return 0.

NOTE:

The cycle must contain atleast two nodes.
There are no self-loops in the graph.
There are no multiple edges between two nodes.
The graph may or may not be connected.
Nodes are numbered from 1 to A.
Your solution will run on multiple test cases. If you are using global variables make sure to clear them.


Problem Constraints

2 <= A <= 105

1 <= M <= min(200000,A*(A-1))

1 <= B[i][0], B[i][1] <= A



Input Format

The first argument given is an integer A representing the number of nodes in the graph.

The second argument given a matrix B of size M x 2 which represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].



Output Format

Return 1 if cycle is present else return 0.



Example Input

Input 1:

 A = 5
 B = [  [1, 2] 
        [4, 1] 
        [2, 4] 
        [3, 4] 
        [5, 2] 
        [1, 3] ]
Input 2:

 A = 5
 B = [  [1, 2]
        [2, 3] 
        [3, 4] 
        [4, 5] ]


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

 The given graph contain cycle 1 -> 3 -> 4 -> 1 or the cycle 1 -> 2 -> 4 -> 1
Explanation 2:

 The given graph doesn't contain any cycle.'''

import sys
sys.setrecursionlimit(int(1e6))

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):

        adj = [[] for i in range(A + 1)]

        for e in B:

            adj[e[0]].append(e[1])
        
        visited = [0 for i in range(A + 1)]
        dfs_call = [0 for i in range(A + 1)]

        for v in range(1, A + 1):
            
            if visited[v] != 1:
                # ans = self.cyclic_dfs_directed_1(v, adj, visited, dfs_call)
                ans = self.cyclic_dfs_directed(v, adj, visited)
                if ans:
                    return 1
        
        return 0

    def cyclic_dfs_directed(self, node, adj, vis):
    
        vis[node] = 1
        
        for nb in adj[node]:
            
            if vis[nb] == 0:
                ans = self.cyclic_dfs_directed(nb, adj, vis)
                
                if ans:
                    return True
            
            elif vis[nb] == 1:
                return True
                
        # Here current dfs call path does not contain a cycle, hence mark as 0
        vis[node] = 0
        return False

    def cyclic_dfs_directed_1(self, node, adj, vis, dfs):
        
        # Mark node visited in main visited array as well as the dfs call array
        vis[node], dfs[node] = 1, 1
        
        for nb in adj[node]:
            
            if vis[nb] == 0:
                # Initiate a recursive call if neighbor has not been visited
                ans = self.cyclic_dfs_directed_1(nb, adj, vis, dfs)
                
                if ans:
                    return True
            # Check if dfs call also has a 1 for nb, i.e. it was already visited and a cycle is present
            elif dfs[nb] == 1:
                return True
            
        # Since cycle is not present, unmark dfs traversal for this call and return false
        dfs[node] = 0
        
        return False
    
# Undirected graph cycle

# DFS

def main(graph, N):
    
    # Build graph
    adj = [[] for i in range(N + 1)]
    
    for e in graph:
        x, y = e[0], e[1]
        adj[x].append(y)
        adj[y].append(x)
    
    # Maintain a visited array
    visited = [0 for i in range(N + 1)]
    
    # Initialize a queue for BFS
    queue = deque()
    
    # Iterate all vertices
    for i in range(1, N + 1):
        
        if visited[i] != 1:
            
            # Call a BFS cycle detector
            ans = isCyclicBFS(i, None, visited, adj, queue)

#             ans = isCyclic(i, None, visited, adj)
            
            if ans:
                # Cycle detected
                return True
    
    # If outside loop, no cycle detected
    return False

# DFS on an undirected graph
def isCyclic(node, parent, vis, adj):
    
    # Mark node as visited
    vis[node] = 1

    # Loop through node's adjacency list
    for nb in adj[node]:
        
        # Call dfs if adjacent node has not been visited
        if vis[nb] != 1:
            return isCyclic(nb, node, vis, adj)
        
        # If already visited and nb is not the node's previous/parent node
        
        # No need to check if vis[nb] == 1 as that is the only other possibility, only check if the neighbor is not
        # the parent
        elif vis[nb] == 1 and nb != parent:

            # Cycle detected
            return True
    
    # If at this point, cycle not detected
    return False

# BFS on an undirected graph
from collections import deque

def isCyclicBFS(node, parent, vis, adj, q):
    
    q.append((node, parent))
    vis[node] = 1

    while q:
        x, y = q.popleft()
        
        # Traverse neighbors
        for nb in adj[x]:
            
            # Check if unvisited
            if vis[nb] != 1:
                
                # Add to queue and mark visited
                q.append((nb, x))
                vis[nb] = 1
            
            # Since nb was previously visited, check if it is not node's parent
            elif nb != y:
                # Cycle detected
                return True
    
    # Cycle not detected
    return False

# DFS directed graph
