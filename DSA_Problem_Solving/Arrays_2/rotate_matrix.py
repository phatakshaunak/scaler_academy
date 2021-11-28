'''Q2. Rotate Matrix
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

You are given a n x n 2D matrix A representing an image.

Rotate the image by 90 degrees (clockwise).

You need to do this in place.

Note: If you end up using an additional array, you will only receive partial score.



Problem Constraints

1 <= n <= 1000



Input Format

First argument is a 2D matrix A of integers



Output Format

Return the 2D rotated matrix.



Example Input

Input 1:

 [
    [1, 2],
    [3, 4]
 ]
Input 2:

 [
    [1]
 ]


Example Output

Output 1:

 [
    [3, 1],
    [4, 2]
 ]
Output 2:

 [
    [1]
 ]


Example Explanation

Explanation 1:

 After rotating the matrix by 90 degree:
 1 goes to 2, 2 goes to 4
 4 goes to 3, 3 goes to 1
Explanation 2:

 2D array remains the ssame as there is only element.'''

class Solution:
    # @param A : list of list of integers
    def solve(self, A):
        
        r = len(A)
        
        # if len(A) == 1:
        #     return A
          
        # Transpose the matrix 
        for i in range(r):
            for j in range(i+1, r):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        
        # Reverse the rows
        for i in range(r):
            s, e = 0, r-1
            
            while s < e:
                
                A[i][s], A[i][e] = A[i][e], A[i][s]
                
                s += 1
                e -= 1
        
        # for i in range(r//2):
            
        #     for j in range(i,r-1-i):
                
        #         temp = A[i][j]
                
        #         A[i][j] = A[r-1-j][i]
                
        #         A[r-1-j][i] = A[r-1-i][r-1-j]   
                
        #         A[r-1-i][r-1-j] = A[j][r-1-i]
                
        #         A[j][r-1-i] = temp
        
        return A

#Time O(n^2), space O(1)