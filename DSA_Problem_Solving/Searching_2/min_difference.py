'''Q1. Minimum Difference
Unsolved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

You are given a 2-D matrix C of size A × B.
You need to build a new 1-D array of size A by taking one element from each row of the 2-D matrix in such a way that the cost of the newly build array is minimized.

Cost of an array is the minimum possible value of the absolute difference between any two adjacent elements of the array.

So if the newly built array is X, element picked from row 1 will become X[1], element picked from row 2 will become X[2], and so on.

Determine the minimum cost of the newly build array.



Problem Constraints

2 <= A <= 1000
2 <= B <= 1000
1 <= C[i][j] <= 106



Input Format

The first argument is an integer A denoting number of rows in the 2-D array.
The second argument is an integer B denoting number of columns in the 2-D array.
The third argument is a 2-D array C of size A x B.



Output Format

Return an integer denoting the minimum cost of the newly build array.



Example Input

Input 1:

 A = 2
 B = 2
 C = [ [8, 4]
      [6, 8] ]
Input 2:

 A = 3
 B = 2
 C = [ [7, 3]
       [2, 1]
       [4, 9] ]


Example Output

Output 1:

 0
Output 2:

 1


Example Explanation

Explanation 1:

 Newly build array : [8, 8]. The minimum cost will be 0 since the absolute difference will be 0(8-8).
Explanation 2:

 Newly build array : [3, 2, 4]. The minimum cost will be 1 since the minimum absolute difference will be 1(3 - 2).'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of list of integers
    # @return an integer
    def solve(self, A, B, C):

        ans = float('inf')
        
        # Sort all rows
        for i in range(A):
            C[i].sort()

        # Task is to start from row 0 to the second last row and find the upper bound and lower bound for each element in the row. Then calculate both differences and update ans with the min value
        # Do this for all the rows and return min value, i.e the ans

        # Iterate over rows 0 to A-1
        for r in range(A-1):
#             print(r)
            # Iterate over columns
            for c in range(B):
                target = C[r][c]

                # Need to check for upper/lower bounds in the next row
                row, col = r + 1, B
                target = C[r][c]

                lb_idx = self.lower_bound(C, target, row, col)
                # ub_idx = self.upper_bound(C, target, row, col)
                
                lb = C[row][lb_idx]
                # ub = C[row][ub_idx]
                
                # print(target, lb, ub)
                ans = min(ans, abs(target - lb))
                
                # if lb_idx < B - 1:
                #     ub = C[row][lb_idx + 1]
                #     ans = min(ans, abs(target - ub))

                # ans = min(ans, abs(target - lb), abs(target - ub))

        return ans

    def lower_bound(self, arr, target, row, col):
        s, e = 0, col - 1
        # If no lower bound (i.e. greatest value <= target, best candidate will be arr[0])
        ans = 0
        while s <= e:
            mid = s + (e - s) // 2
            
            if arr[row][mid] > target:
                e = mid - 1
            
            else:
                ans = mid
                s = mid + 1
        
        return ans

    def upper_bound(self, arr, target, row, col):
        s, e = 0, col - 1
        # If no upper bound (i.e. smallest value >= target, best candidate will be arr[-1])
        ans = e
        while s <= e:
            mid = s + (e - s) // 2
            
            if arr[row][mid] >= target:
                ans = mid
                e = mid - 1
            
            else:
                s = mid + 1
        
        return ans