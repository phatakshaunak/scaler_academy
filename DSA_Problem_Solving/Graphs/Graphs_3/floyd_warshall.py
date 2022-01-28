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

        # Update -1's to float('inf')
        for r in range(N):

            for c in range(N):

                if A[r][c] == -1:
                    A[r][c] = float('inf')

        # Relax each intermediate edge (outer loop does that, inner two loops consider all matrix elements as edges)

        for rl in range(N):

            for r in range(N):

                for c in range(N):
                    
                    # Avoiding diagonals or when row or column are equal to the node being relaxed
                    if r != c and r != rl and c != rl:

                        if A[r][c] > A[r][rl] + A[rl][c]:
                            A[r][c] = A[r][rl] + A[rl][c]

                        # Fails if min is used: https://www.scaler.com/help_requests/56056/
                        # A[r][c] = min(A[r][c], A[r][rl] + A[rl][c])
        
        # Update float('inf') to -1
        for r in range(N):

            for c in range(N):

                if A[r][c] == float('inf'):
                    A[r][c] = -1

        return A