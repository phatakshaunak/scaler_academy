'''Q2. Unique Paths III
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a matrix of integers A of size N x M . There are 4 types of squares in it:

1. 1 represents the starting square.  There is exactly one starting square.
2. 2 represents the ending square.  There is exactly one ending square.
3. 0 represents empty squares we can walk over.
4. -1 represents obstacles that we cannot walk over.
Find and return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

Note: Rows are numbered from top to bottom and columns are numbered from left to right.



Problem Constraints

2 <= N * M <= 20
-1 <= A[i] <= 2



Input Format

The first argument given is the integer matrix A.



Output Format

Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.



Example Input

Input 1:

A = [   [1, 0, 0, 0]
        [0, 0, 0, 0]
        [0, 0, 2, -1]   ]
Input 2:

A = [   [0, 1]
        [2, 0]    ]


Example Output

Output 1:

2
Output 2:

0


Example Explanation

Explanation 1:

We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Explanation 1:

Answer is evident here.'''

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):


        '''
        Initially get the count of zeros and start position. Then backtrack in four directions marking each visited cell as -1. If a zero is encountered, count it and mark as -1. Thus if 2 is reached and 
        counted zeros is equal to the total zeros, that is a valid path.
        '''

        N, M = len(A), len(A[0])
        zr = 0
        
        # Get count of zeros and start position
        for i in range(N):
            for j in range(M):

                if A[i][j] == 1:
                    s_i, s_j = i, j
                
                if A[i][j] == 0:
                    zr += 1
        
        dirc = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        ans = [0]

        # Start ct at -1 as marking 1 as -1 should not count to the count of total zeros
        self.rec(A, N, M, dirc, s_i, s_j, -1, zr, ans)

        return ans[0]
    
    def rec(self, A, N, M, dirc, r, c, ct, zr, ans):
        
        # Boundary conditions for out of range row and columns as well as encountering an obstacle or a marked visited zero or 1.
        if r < 0 or c < 0 or r == N or c == M or A[r][c] == -1:
            return
        
        if A[r][c] == 2:
            if ct == zr:
                ans[0] += 1
            return

        for d in dirc:
            
            tmp = A[r][c]
            A[r][c] = -1
            ct += 1

            self.rec(A, N, M, dirc, r + d[0], c + d[1], ct, zr, ans)

            if tmp == 1:
                A[r][c] = 1
            # if tmp == 0:
            else:
                A[r][c] = 0

            ct -= 1