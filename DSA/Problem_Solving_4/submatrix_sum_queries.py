'''Q1. Sub-matrix Sum Queries
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a matrix of integers A of size N x M and multiple queries Q, for each query find and return the submatrix sum.

Inputs to queries are top left (b, c) and bottom right (d, e) indexes of submatrix whose sum is to find out.

NOTE:

Rows are numbered from top to bottom and columns are numbered from left to right.
Sum may be large so return the answer mod 109 + 7.


Problem Constraints

1 <= N, M <= 1000
-100000 <= A[i] <= 100000
1 <= Q <= 100000
1 <= B[i] <= D[i] <= N
1 <= C[i] <= E[i] <= M



Input Format

The first argument given is the integer matrix A.
The second argument given is the integer array B.
The third argument given is the integer array C.
The fourth argument given is the integer array D.
The fifth argument given is the integer array E.
(B[i], C[i]) represents the top left corner of the i'th query.
(D[i], E[i]) represents the bottom right corner of the i'th query.



Output Format

Return an integer array containing the submatrix sum for each query.



Example Input

Input 1:

 A = [   [1, 2, 3]
         [4, 5, 6]
         [7, 8, 9]   ]
 B = [1, 2]
 C = [1, 2]
 D = [2, 3]
 E = [2, 3]
Input 2:

 A = [   [5, 17, 100, 11]
         [0, 0,  2,   8]    ]
 B = [1, 1]
 C = [1, 4]
 D = [2, 2]
 E = [2, 4]


Example Output

Output 1:

 [12, 28]
Output 2:

 [22, 19]


Example Explanation

Explanation 1:

 For query 1: Submatrix contains elements: 1, 2, 4 and 5. So, their sum is 12.
 For query 2: Submatrix contains elements: 5, 6, 8 and 9. So, their sum is 28.
Explanation 2:

 For query 1: Submatrix contains elements: 5, 17, 0 and 0. So, their sum is 22.
 For query 2: Submatrix contains elements: 11 and 8. So, their sum is 19.'''

class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E):
        
        mod = int(1e9+7)
        # First generate a prefix sum matrix.
        
        row, col = len(A), len(A[0])
        
        # Initialize a prefix sum matrix
        
        pf_matrix = [[0]*col for i in range(row)]
        
        # Fill prefix sum matrix. Initially compute a row wise prefix sum matrix.
        
        for x in range(row):
            for y in range(col):
                
                if y == 0:
                    pf_matrix[x][y] = A[x][y] % mod
                
                else:
                    pf_matrix[x][y] = (pf_matrix[x][y-1] % mod + A[x][y] % mod) % mod
                
        # Then compute a column sum
        
        for r in range(1,row):
            for c in  range(col):
                
                pf_matrix[r][c] = (pf_matrix[r-1][c] % mod + pf_matrix[r][c] % mod) % mod
        
        q = len(B)
        ans = []
        for qr in range(q):
            
            tl1, tl2 = B[qr] - 1, C[qr] - 1
            br1, br2 = D[qr] - 1, E[qr] - 1
            
            if tl1 == 0 and tl2 == 0:
                ans.append(pf_matrix[br1][br2] % mod)
                
            elif tl1 == 0:
                pf_val = ((pf_matrix[br1][br2] % mod) - (pf_matrix[br1][tl2 - 1] % mod)) % mod
                ans.append(pf_val)
            
            elif tl2 == 0:
                pf_val = ((pf_matrix[br1][br2] % mod) - (pf_matrix[tl1 - 1][br2] % mod)) % mod
                ans.append(pf_val)
                
            else:
                pf_val = ((pf_matrix[br1][br2] % mod)  - (pf_matrix[tl1 - 1][br2] % mod) - (pf_matrix[br1][tl2 - 1] % mod) + (pf_matrix[tl1 - 1][tl2 - 1] % mod)) % mod
            
                ans.append(pf_val)
            
        return ans
            
'''
Considering zero based indexing, added three conditions for when both top left row/col are zero as well as when either row / col are zero for top left.
'''
