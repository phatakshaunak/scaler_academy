'''Q6. Another Count Rectangles
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a sorted array of distinct integers A and an integer B, find and return how many rectangles with distinct configurations can be created using elements of this array as length and breadth whose area is lesser than B.

(Note that a rectangle of 2 x 3 is different from 3 x 2 if we take configuration into view)



Problem Constraints

1 <= |A| <= 100000
1 <= A[i] <= 109
1 <= B <= 109



Input Format

The first argument given is the integer array A.

The second argument given is integer B.



Output Format

Return the number of rectangles with distinct configurations with area less than B modulo (109 + 7).



Example Input

Input 1:

 A = [1, 2]
 B = 5
Input 2:

 A = [1, 2]
 B = 1


Example Output

Output 1:

 4
Output 2:

 0


Example Explanation

Explanation 1:

 All 1X1, 2X2, 1X2 and 2X1 have area less than 5.
Explanation 2:

 No Rectangle is valid.'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        i, j = 0, len(A) - 1
        ans, m = 0, int(1e9+7)
        while i <= j:
            
            if A[i] * A[j] < B:
                
                # Count all pairs with A[i] until A[j] and subtract double counted A[i]*A[i]
                ans = (ans % m + (2 * (j - i) + 1) % m) % m
                i += 1
            else:
                j -= 1
        
        return ans
