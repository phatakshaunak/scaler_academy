'''Q4. Maximum Sum
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

You are given an array A of N integers and three integers B, C, and D.

You have to find the maximum value of A[i]*B + A[j]*C + A[k]*D, where 1 <= i <= j <= k <= N.



Problem Constraints

1 <= N <= 105

-10000 <= A[i], B, C, D <= 10000



Input Format

First argument is an array A
Second argument is an integer B
Third argument is an integer C
Fourth argument is an integer D



Output Format

Return an Integer S, i.e maximum value of (A[i] * B + A[j] * C + A[k] * D), where 1 <= i <= j <= k <= N.



Example Input

Input 1:

 A = [1, 5, -3, 4, -2]
 B = 2
 C = 1
 D = -1
Input 2:

 A = [3, 2, 1]
 B = 1
 C = -10
 D = 3


Example Output

Output 1:

 18
Output 2:

 -4


Example Explanation

Explanation 1:

 If you choose i = 2, j = 2, and k = 3 then we will get
 A[2]*B + A[2]*C + A[3]*D = 5*2 + 5*1 + (-3)*(-1) = 10 + 5 + 3 = 18
Explanation 2:

 If you choose i = 1, j = 3, and k = 3 then we will get
 A[1]*B + A[3]*C + A[3]*D = (3*1) + (-10*1) + (3*1) = 3 - 10 + 3 = -4'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):

        # l1, l2, l3 = float('-inf'), float('-inf'), float('-inf')

        # for val in A:
        #     l1 = max(l1, B * val)
        #     l2 = max(l2, l1 + C * val)
        #     l3 = max(l3, l2 + D * val)
        
        # return l3

        p1 = [float('-inf')] * (len(A) + 1)
        p2 = [float('-inf')] * (len(A) + 1)
        p3 = [float('-inf')] * (len(A) + 1)

        for i in range(len(A)):

            p1[i + 1] = max(p1[i], A[i] * B)

            p2[i + 1] = max(p2[i], p1[i + 1] + A[i] * C)

            p3[i + 1] = max(p3[i], p2[i + 1] + A[i] * D)

        return p3[-1]