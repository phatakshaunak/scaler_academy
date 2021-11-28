'''Q4. Pascal Triangle
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Write a program to input an integer N from user and print pascal triangle up to N rows.



Problem Constraints

1 <= N <= 25



Input Format

First line is an integer N.



Output Format

N lines whose each row contains N+1 space separated integers.



Example Input

Input 1:

3
Input 2:

5


Example Output

Output 1:

1 0 0 
1 1 0 
1 2 1 
Output 2:

1 0 0 0 0
1 1 0 0 0
1 2 1 0 0
1 3 3 1 0
1 4 6 4 1 


Example Explanation

Explanation 1:

Row 1 = 1 0 0 0 0
Row 2 = 1C0 1C1 0 0 0= 1 1 0 0 0
Row 3 = 2C0 2C1 2C2 0 0= 1 2 1 0 0
Row 4 = 3C0 3C1 3C2 3C3 0= 1 3 3 1 0'''

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        # if A == 1:
        #     return[[1]]
        
        if A == 0:
            return []
            
        arr = [[0]*A for r in range(A)]
        
        arr[0][0] = 1
        
        for i in range(1,A):
            for j in range(0,i+1):
                if j == 0:
                    arr[i][j] = 1
                else:
                    arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
        
        return arr