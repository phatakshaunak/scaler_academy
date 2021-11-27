'''
Q3. Pattern Printing -2
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Print a Pattern According to The Given Value of A.

Example: For A = 3 pattern looks like:

    1
  2 1
3 2 1


Problem Constraints

1 <= A <= 1000


Input Format

First and only argument is an integer denoting A.



Output Format

Return a two-dimensional array where each row in the returned array represents a row in the pattern.



Example Input

Input 1:

 A = 3
Input 2:

 A = 4


Example Output

Output :1

 [ 
   [0, 0, 1]
   [0, 2, 1]
   [3, 2, 1]
 ]
Output 2:

 [ 
   [0, 0, 0, 1]
   [0, 0, 2, 1]
   [0, 3, 2, 1]
   [4, 3, 2, 1]
 ]


Example Explanation

Explanation 2:

 
 For A = 4 pattern looks like:  
                                   1
                                 2 1
                               3 2 1
                             4 3 2 1
 So we will return it as two-dimensional array. 
 Row 1 contains 3 spaces and 1 integer so spaces will be considered as 0 in the output.'''

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        
        N = A
        
        arr = [[0]*N for i in range(N)]
        
        for i in range(N):
            c = 1
            for j in range((N-1), (N-1)-i-1, -1):
                arr[i][j] = c
                c += 1
        return arr

