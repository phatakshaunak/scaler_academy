'''Q3. Distance of nearest cell
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a matrix of integers A of size N x M consisting of 0 or 1.

For each cell of the matrix find the distance of nearest 1 in the matrix.

Distance between two cells (x1, y1) and (x2, y2) is defined as |x1 - x2| + |y1 - y2|.

Find and return a matrix B of size N x M which defines for each cell in A distance of nearest 1 in the matrix A.

NOTE: There is atleast one 1 is present in the matrix.



Problem Constraints

1 <= N, M <= 1000

0 <= A[i][j] <= 1



Input Format

The first argument given is the integer matrix A.



Output Format

Return the matrix B.



Example Input

Input 1:

 A = [
       [0, 0, 0, 1]
       [0, 0, 1, 1] 
       [0, 1, 1, 0]
     ]
Input 2:

 A = [
       [1, 0, 0]
       [0, 0, 0]
       [0, 0, 0]  
     ]


Example Output

Output 1:

 [ 
   [3, 2, 1, 0]
   [2, 1, 0, 0]
   [1, 0, 0, 1]   
 ]
Output 2:

 [
   [0, 1, 2]
   [1, 2, 3]
   [2, 3, 4] 
 ]


Example Explanation

Explanation 1:

 A[0][0], A[0][1], A[0][2] will be nearest to A[0][3].
 A[1][0], A[1][1] will be nearest to A[1][2].
 A[2][0] will be nearest to A[2][1] and A[2][3] will be nearest to A[2][2].
Explanation 2:

 There is only a single 1. Fill the distance from that 1.
'''

from collections import deque
class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):

        q = deque()

        n, m = len(A), len(A[0])

        for i in range(n):

            for j in range(m):

                if A[i][j] == 1:
                    q.append((i, j, 0))
        
        ans = [[0 for i in range(m)] for j in range(n)]

        drc = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while q:

            x, y, dist = q.popleft()

            for d in drc:

                c_x, c_y = x + d[0], y + d[1]

                if c_x >= 0 and c_y >= 0 and c_x < n and c_y < m:

                    if A[c_x][c_y] == 0:
                        
                        q.append((c_x, c_y, dist + 1))
                        ans[c_x][c_y] = dist + 1
                        A[c_x][c_y] = 1
        
        return ans