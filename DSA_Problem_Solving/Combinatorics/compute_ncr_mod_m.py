'''Q2. Compute nCr % m
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given three integers A, B and C, where A represents n, B represents r and C represents m, find and return the value of nCr % m where nCr % m = (n!/((n-r)!*r!))% m.

x! means factorial of x i.e. x! = 1 * 2 * 3... * x.



Problem Constraints

1 <= A * B <= 106

1 <= B <= A

1 <= C <= 106



Input Format

The first argument given is integer A ( = n).
The second argument given is integer B ( = r).
The third argument given is integer C ( = m).


Output Format

Return the value of nCr % m.



Example Input

Input 1:

 A = 5
 B = 2
 C = 13
Input 2:

 A = 6
 B = 2
 C = 13


Example Output

Output 1:

 10
Output 2:

 2


Example Explanation

Explanation 1:

 The value of 5C2 % 11 is 10.
Explanation 2:

 The value of 6C2 % 13 is 2.'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        
        fact = [[0]*(B+1) for i in range(A+1)]
        fact[0][0] = 1
        
        for c_ in range(1,A+1):
            for r_ in range(B+1):
                if r_ == 0:
                    fact[c_][r_] = 1
                else:
                    fact[c_][r_] = (fact[c_-1][r_-1] % C + fact[c_-1][r_] % C) % C
        
        return fact[A][B]
