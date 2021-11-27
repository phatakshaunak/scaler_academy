'''Q5. Period of a string
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a string A of length N consisting of lowercase alphabets. Find the period of the string.

Period of the string is the minimum value of k (k >= 1), that satisfies A[i] = A[i % k] for all valid i.



Problem Constraints

1 <= N <= 106



Input Format

First and only argument is a string A of length N.



Output Format

Return an integer, denoting the period of the string.



Example Input

Input 1:

 A = "abababab"
Input 2:

 A = "aaaa"


Example Output

Output 1:

 2
Output 2:

 1


Example Explanation

Explanation 1:

 Period of the string will be 2: 
 Since, for all i, A[i] = A[i%2]. 
Explanation 2:

 Period of the string will be 1.'''

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        N = len(A)
        Z_arr = self.generate_Z(A)

        for idx in range(1, N):
            if idx + Z_arr[idx] == N:
                return idx
        
        return N

    def generate_Z(self, S):
        M = len(S)
        L, R = 0, 0
        Z = [0 for i in range(M)]
        Z[0] = M

        for i in range(1, M):

            if i > R:
                L, R = i, i
                while R < M and S[R] == S[R-L]:
                    R += 1
                R -= 1
                Z[i] = (R - L + 1)
            
            else:
                j = (i - L)

                if Z[j] < (R - i + 1):
                    Z[i] = Z[j]
                
                else:
                    L = i
                    while R < M and S[R] == S[R-L]:
                        R += 1
                    R -= 1
                    Z[i] = (R - L + 1)

        return Z