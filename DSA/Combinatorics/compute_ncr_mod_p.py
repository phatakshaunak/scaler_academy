'''Q3. Compute nCr % p
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given three integers A, B and C, where A represents n, B represents r and C represents p and p is a prime number greater than equal to n, find and return the value of nCr % p where nCr % p = (n! / ((n-r)! * r!)) % p.

x! means factorial of x i.e. x! = 1 * 2 * 3... * x.

note: For this problem, we are considering 1 as a prime.



Problem Constraints

1 <= A <= 106
1 <= B <= A
A <= C <= 109+7


Input Format

The first argument given is the integer A ( = n).
The second argument given is the integer B ( = r).
The third argument given is the integer C ( = p).



Output Format

Return the value of nCr % p.



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

 nCr( n=5 and r=2) = 10.
 p=13. Therefore, nCr%p = 10.'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        
        # As (n)C(r) and (n)C(n-r) are the same
        B = min(B,A-B)
        
        def bin_exp(num,b,p):
            ans = 1
            while b >= 1:
                if b&1:
                    ans = (ans % p * num % p) % p
                    num = (num % p * num % p) % p
                    b = b // 2
                else:
                    num = (num % p * num % p) % p
                    b = b // 2
            
            return ans
        
        i = 0
        num, den = 1,1
        while i < B:
            num = (num % C * (A-i) % C) % C 
            den = (den % C * (B-i) % C) % C
            i += 1
        
        return (num * bin_exp(den,C-2,C)) % C