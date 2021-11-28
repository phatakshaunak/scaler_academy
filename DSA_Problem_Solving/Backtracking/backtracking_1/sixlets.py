'''Q1. SIXLETS
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a array of integers A of size N and an integer B.

Return number of non-empty subsequences of A of size B having sum <= 1000.



Problem Constraints

1 <= N <= 20

1 <= A[i] <= 1000

1 <= B <= N



Input Format

The first argument given is the integer array A.

The second argument given is the integer B.



Output Format

Return number of subsequences of A of size B having sum <= 1000.



Example Input

Input 1:

    A = [1, 2, 8]
    B = 2
Input 2:

    A = [5, 17, 1000, 11]
    B = 4


Example Output

Output 1:

3
Output 2:

0


Example Explanation

Explanation 1:

 {1, 2}, {1, 8}, {2, 8}
Explanation 1:

 No valid subsequence'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def solve(self,A, B):
        
        def gen_seq_1000(A,B,sm,ct,i,ans):
    
            if sm > 1000:
                return
            if ct == B:
                ans[0] += 1
                # print('ans',ans, 'sum', sm)
                return
            if i == len(A):
                return

            gen_seq_1000(A,B,sm+A[i],ct+1,i+1,ans)
            gen_seq_1000(A,B,sm,ct,i+1,ans)
        
        ans = [0]
        gen_seq_1000(A,B,0,0,0,ans)
        
        return ans[0]