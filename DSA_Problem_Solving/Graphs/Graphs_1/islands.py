'''Q2. Number of islands
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a matrix of integers A of size N x M consisting of 0 and 1. A group of connected 1's forms an island. From a cell (i, j) such that A[i][j] = 1 you can visit any cell that shares a corner with (i, j) and value in that cell is 1.

More formally, from any cell (i, j) if A[i][j] = 1 you can visit:

(i-1, j) if (i-1, j) is inside the matrix and A[i-1][j] = 1.
(i, j-1) if (i, j-1) is inside the matrix and A[i][j-1] = 1.
(i+1, j) if (i+1, j) is inside the matrix and A[i+1][j] = 1.
(i, j+1) if (i, j+1) is inside the matrix and A[i][j+1] = 1.
(i-1, j-1) if (i-1, j-1) is inside the matrix and A[i-1][j-1] = 1.
(i+1, j+1) if (i+1, j+1) is inside the matrix and A[i+1][j+1] = 1.
(i-1, j+1) if (i-1, j+1) is inside the matrix and A[i-1][j+1] = 1.
(i+1, j-1) if (i+1, j-1) is inside the matrix and A[i+1][j-1] = 1.
Return the number of islands.

NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.



Problem Constraints

1 <= N, M <= 100

0 <= A[i] <= 1



Input Format

The only argument given is the integer matrix A.



Output Format

Return the number of islands.



Example Input

Input 1:

 A = [ 
       [0, 1, 0]
       [0, 0, 1]
       [1, 0, 0]
     ]
Input 2:

 A = [   
       [1, 1, 0, 0, 0]
       [0, 1, 0, 0, 0]
       [1, 0, 0, 1, 1]
       [0, 0, 0, 0, 0]
       [1, 0, 1, 0, 1]    
     ]


Example Output

Output 1:

 2
Output 2:

 5


Example Explanation

Explanation 1:

 The 1's at position A[0][1] and A[1][2] forms one island.
 Other is formed by A[2][0].
Explanation 2:

 There 5 island in total.'''

from collections import deque
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):

        n, m = len(A), len(A[0])

        q = deque()

        vis = [[0 for i in range(m)] for j in range(n)]
        
        drc = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        isl = 0

        for i in range(n):
            
            for j in range(m):

                if A[i][j] == 1 and vis[i][j] == 0:

                    isl += 1

                    q.append((i, j))

                    self.bfs(vis, q, drc, n, m, A)
        
        return isl

    def bfs(self, vis, q, drc, r, c, M):

        while q:

            x, y = q.popleft()
            
            vis[x][y] = 1

            for d in drc:

                c_x, c_y = x + d[0], y + d[1]

                if self.check(c_x, c_y, vis, r, c, M):

                    q.append((c_x, c_y))

                    vis[c_x][c_y] = 1
    
    def check(self, x, y, vis, r, c, M):

        return x >= 0 and x < r and y >= 0 and y < c and vis[x][y] == 0 and M[x][y] == 1