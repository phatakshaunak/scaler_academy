'''Q4. Floyd Warshall Algorithm
Unsolved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a matrix of integers A of size N x N, where A[i][j] represents the weight of directed edge from i to j (i ---> j).

If i == j, A[i][j] = 0, and if there is no directed edge from vertex i to vertex j, A[i][j] = -1.

Return a matrix B of size N x N where B[i][j] = shortest path from vertex i to vertex j.

If there is no possible path from vertex i to vertex j , B[i][j] = -1

Note: Rows are numbered from top to bottom and columns are numbered from left to right.



Problem Constraints

1 <= N <= 200
-1 <= A[i][j] <= 1000000


Input Format

The first and only argument given is the integer matrix A.


Output Format

Return a matrix B of size N x N where B[i][j] = shortest path from vertex i to vertex j
If there is no possible path from vertex i to vertex j, B[i][j] = -1.


Example Input

A = [ [0 , 50 , 39]
          [-1 , 0 , 1]
          [-1 , 10 , 0] ]


Example Output

[ [0 , 49 , 39 ]
   [-1 , 0 , -1 ]
   [-1 , 10 , 0 ] ]


Example Explanation

Shortest Path from 1 to 2 would be 1 ---> 3 ---> 2 and not directly from 1 to 2,
All remaining distances remains same.
'''

class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):

        N = len(A)

        # Goal is to relax each intermediate edge (outer loop does that, inner two loops consider all matrix elements as edges)

        # For self edges, the value will be zero, a separate case could have been written but can be handled by this code

        for rl in range(N):

            for r in range(N):

                for c in range(N):

                    curr = A[r][c] if A[r][c] != -1 else float('inf')

                    i1 = A[r][rl] if A[r][rl] != -1 else float('inf')

                    i2= A[rl][c] if A[rl][c] != -1 else float('inf')
                    
                    ans = min(curr, i1 + i2)

                    A[r][c] = ans if ans != float('inf') else -1

        return A