'''Q2. Very Large Power
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given two Integers A, B. You have to calculate (A ^ (B!)) % (1e9 + 7).

"^" means power ,

"%" means "mod", and

"!" means factorial.



Problem Constraints

1 <= A, B <= 5e5



Input Format

First argument is the integer A

Second argument is the integer B



Output Format

Return one integer, the answer to the problem



Example Input

Input 1:

A = 1
B = 1
Input 2:

A = 2
B = 2


Example Output

Output 1:

1
Output 2:

4


Example Explanation

Explanation 1:

 1! = 1. Hence 1^1 = 1.
Explanation 2:

 2! = 2. Hence 2^2 = 4.'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        m = int(1e9+7)
        
        def fact_mod(a,m):
            ans = 1
            while a > 1:
                ans = (ans % m * a % m) % m
                a -= 1
            return ans
        
        def pow_exp(a,b,m):
            ans = 1
            while b >= 1:
                if b&1:
                    ans = (a % m * ans % m) % m
                    a = (a % m * a % m) % m
                    b = b // 2
                else:
                    a = (a % m * a % m) % m
                    b = b // 2
            return ans
        
        r = fact_mod(B,m-1)
        
        return pow_exp(A,r,m)