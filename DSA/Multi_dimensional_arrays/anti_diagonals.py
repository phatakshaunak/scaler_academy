'''Q3. Anti Diagonals
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Give a N * N square matrix A, return an array of its anti-diagonals. Look at the example for more details.


Problem Constraints

1<= N <= 1000
1<= A[i][j] <= 1e9


Input Format

First argument is an integer N, denoting the size of square 2D matrix.
Second argument is a 2D array A of size N * N.


Output Format

Return a 2D integer array of size (2 * N-1) * N, representing the anti-diagonals of input array A.
The vacant spaces in the grid should be assigned to 0.


Example Input

Input 1:
3
1 2 3
4 5 6
7 8 9
Input 2:

1 2
3 4


Example Output

Output 1:
1 0 0
2 4 0
3 5 7
6 8 0
9 0 0
Output 2:

1 0
2 3
4 0


Example Explanation

For input 1:
The first anti diagonal of the matrix is [1 ], the rest spaces shoud be filled with 0 making the row as [1, 0, 0].
The second anti diagonal of the matrix is [2, 4 ], the rest spaces shoud be filled with 0 making the row as [2, 4, 0].
The third anti diagonal of the matrix is [3, 5, 7 ], the rest spaces shoud be filled with 0 making the row as [3, 5, 7].
The fourth anti diagonal of the matrix is [6, 8 ], the rest spaces shoud be filled with 0 making the row as [6, 8, 0].
The fifth anti diagonal of the matrix is [9 ], the rest spaces shoud be filled with 0 making the row as [9, 0, 0].
For input 2:

The first anti diagonal of the matrix is [1 ], the rest spaces shoud be filled with 0 making the row as [1, 0, 0].
The second anti diagonal of the matrix is [2, 4 ], the rest spaces shoud be filled with 0 making the row as [2, 4, 0].
The third anti diagonal of the matrix is [3, 0, 0 ], the rest spaces shoud be filled with 0 making the row as [3, 0, 0].'''

class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        
        N = len(A)
        
        # diagonals = [[] for i in range(2*N-1)]
    
        # for i in range(N):
        #     for j in range(N):
        #         diagonals[i+j].append(A[i][j])
        
        # for i in diagonals:
            
        #     col = len(i)
        #     while col < N:
        #         i.append(0)
        #         col += 1
        
        diagonals = []
        # Consider upper diagonals where the row index increments and column index decrements. We move along the columns for these diagonals. These elements start from the first row
        
        for i in range(N):
            row = []
            r = 0
            c = i
            
            while (c >= 0):
                
                row.append(A[r][c])
                r += 1
                c -= 1
            
            diagonals.append(row)
        
        # Next consider lower diagonals which always start on the N-1th column. Here we start from row 1 and column N-1 and traverse all such diagonals. We move along the rows for these diagonals
        
        for i in range(1,N):
            row = []
            r = i
            c = N-1
            
            while (r<=N-1):
                row.append(A[r][c])
                r += 1
                c -= 1
                
            diagonals.append(row)
        
        for i in diagonals:
            
            col = len(i)
            while col < N:
                i.append(0)
                col += 1
        
        return diagonals
            