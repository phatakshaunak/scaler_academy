'''Q4. Russian Doll Envelopes
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a matrix of integers A of size N x 2 describing dimensions of N envelopes, where A[i][0] denotes the height of the ith envelope and A[i][1] denotes the width of the ith envelope.

One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

Find the maximum number of envelopes you can put one inside other.



Problem Constraints

1 <= N <= 1000
1 <= A[i][0], A[i][1] <= 109



Input Format

The only argument given is the integer matrix A.



Output Format

Return an integer denoting the maximum number of envelopes you can put one inside other.



Example Input

Input 1:

 A = [ 
         [5, 4]
         [6, 4]
         [6, 7]
         [2, 3]  
     ]
Input 2:

 A = [     '
         [8, 9]
         [8, 18]    
     ]


Example Output

Output 1:

 3
Output 2:

 1


Example Explanation

Explanation 1:

 Step 1: put [2, 3] inside [5, 4]
 Step 2: put [5, 4] inside [6, 7]
 3 envelopes can be put one inside other.
Explanation 2:

 No envelopes can be put inside any other so answer is 1.'''

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):

        # Sort in increasing order by height and decreasing order by width if there is a tie in height
        # Then apply LIS for the width and return maximum value

        # A = sorted(A, key = lambda pair: [pair[0], -pair[1]])

        # Another way is to sort one dimension 
        #and simply check if the left height dimensions are smaller than current height
        
        A.sort()
        ans = 1

        dp = [0 for i in range(len(A))]
        dp[0] = 1

        for i in range(1, len(A)):

            curr = 1

            for j in range(i):

                if A[j][1] < A[i][1] and A[i][0] > A[j][0]:
                    curr = max(curr, 1 + dp[j])
            
            dp[i] = curr
            ans = max(ans, dp[i])
        
        return ans
    
    # TC O(N^2), SC O(N)