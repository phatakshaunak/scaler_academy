'''Q3. Prime Modulo Inverse
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given two integers A and B. Find the value of A-1 mod B where B is a prime number and gcd(A, B) = 1.

A-1 mod B is also known as modular multiplicative inverse of A under modulo B.



Problem Constraints

1 <= A <= 109
1<= B <= 109
B is a prime number



Input Format

First argument is an integer A.
Second argument is an integer B.



Output Format

Return an integer denoting the modulor inverse



Example Input

Input 1:

 A = 3
 B = 5
Input 2:

 A = 6
 B = 23


Example Output

Output 1:

 2
Output 2:

 4


Example Explanation

Explanation 1:

 Let's say A-1 mod B = X, then (A * X) % B = 1.
 3 * 2 = 6, 6 % 5 = 1.
Explanation 2:

 Similarly, (6 * 4) % 23 = 1.'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        def pow_exp_mod(a,b,m):
            ans = 1
            while b >= 1:
                if b&1:
                    ans = ((ans % m) * (a % m)) % m
                    a = (a%m * a%m)%m
                    b = b // 2
                else:
                    a = (a%m * a%m)%m
                    b = b // 2
            return ans%m
        
        return pow_exp_mod(A,B-2,B)
