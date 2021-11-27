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
        
        #Case for a 1X1 array
        if len(A) == 1:
            return A
        
        N = len(A)
        
        def transpose(arr, N):
            
            for i in range(N):
                for j in range(i+1,N):
                    arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
        
        transpose(A,N)
        
        for i in range(N):
            
            l, r = 0, N-1
            
            while l < r:
                A[i][l], A[i][r] = A[i][r], A[i][l]
                l += 1
                r -= 1
        
        return A

# O(N*N) time, O(1) space
        