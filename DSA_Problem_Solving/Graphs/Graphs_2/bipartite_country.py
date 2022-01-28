'''Q4. Construct Roads
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

A country consist of N cities connected by N - 1 roads. King of that country want to construct maximum number of roads such that the new country formed remains bipartite country.

Bipartite country is a country, whose cities can be partitioned into 2 sets in such a way, that for each road (u, v) that belongs to the country, u and v belong to different sets. Also, there should be no multiple roads between two cities and no self loops.

Return the maximum number of roads king can construct. Since the answer could be large return answer % 109 + 7.

NOTE: All cities can be visited from any city.



Problem Constraints

1 <= A <= 105

1 <= B[i][0], B[i][1] <= N



Input Format

First argument is an integer A denoting the number of cities, N.

Second argument is a 2D array B of size (N-1) x 2 denoting the initial roads i.e. there is a road between cities B[i][0] and B[1][1] .



Output Format

Return an integer denoting the maximum number of roads king can construct.



Example Input

Input 1:

 A = 3
 B = [
       [1, 2]
       [1, 3]
     ]
Input 2:

 A = 5
 B = [
       [1, 3]
       [1, 4]
       [3, 2]
       [3, 5]
     ]


Example Output

Output 1:

 0
Output 2:

 2


Example Explanation

Explanation 1:

 We can't construct any new roads such that the country remains bipartite.
Explanation 2:

 We can add two roads between cities (4, 2) and (4, 5).'''

from collections import deque

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):

        adj = [[] for i in range(A + 1)]
        col = [-1 for i in range(A + 1)]

        for e in B:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        
        q = deque()

        for i in range(1, A + 1):

            if col[i] == -1:
                col[i] = 0
                q.append(i)

                self.bfs_bipartite(adj, col, q)
                
                # This is a check if a graph is not bipartite. Not applicable here
                # if not ans:
                #     return 0
        
        # Here count elements in both sets as country is bipartite
        zero, one = 0, 0
        for i in range(1, A + 1):
            
            if col[i] == 0:
                zero += 1
            
            else:
                one += 1
        
        edges = len(B)

        m = int(1e9 + 7)

        ans = ((zero * one) - edges) % m

        return ans
        '''
        As the tree is bipartite, it can be two-colored. Run the 2-color algorithm and divide into two sets.
        Then, count elements in both color sets and multiply to get maximum roads possible, subtract given edges from this amount to get the answer
        '''
    def bfs_bipartite(self, adj, col, q):

        while q:
            top = q.popleft()

            for nb in adj[top]:

                if col[nb] == -1:
                    col[nb] = col[top] ^ 1
                    q.append(nb)
                
                # This condition checks if graph is bipartite or not, not valid as given graph is already bipartite
                # elif col[nb] == col[top]:
                #     return False
        
        # return