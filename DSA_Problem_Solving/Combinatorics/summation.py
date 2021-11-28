'''Q3. SUMMATION
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an integer A.

Calculate the sum = (ACr) * (r) * (r - 1) * (2r-2) for all r from 0 to A.

Return sum % 109 + 7.



Problem Constraints

2 <= A <= 106



Input Format

The first and only argument given is the integer A.



Output Format

Return a single integer denoting sum % 109 + 7.



Example Input

Input 1:

 A = 3
Input 2:

 A = 4


Example Output

Output 1:

 18
Output 2:

 108


Example Explanation

Explaination 1:

 (ACr) * (r) * (r - 1) * (2r-2)
 r = 0, (1) * (0) * (1) * (1/4) = 0
 r = 1, (3) * (1) * (0) * (1/2) = 0
 r = 2, (3) * (2) * (1) * (1) = 6
 r = 3, (1) * (3) * (2) * (2) = 12
 sum = 18'''

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        
        m = int(1e9+7)
        
        def bin_exp(n,p,m):
            ans = 1
            while p >= 1:
                if p&1:
                    ans = (ans % m * n % m) % m
                    n = (n % m * n % m) % m
                else:
                    n = (n % m * n % m) % m
                p = p // 2
            return ans
        
        def ncr_mod(n,r,m):
            if r == 0 or r == n:
                return 1 % m
            elif r == 1:
                return n % m
            
            ans, num, den = 1, 1, 1
            
            for i in range(r):
                num = (num % m * (n-i) % m) % m
                den = (den % m * (r-i) % m) % m
            
            ans = (num * bin_exp(den, m-2, m)) % m
            
            return ans
            
            # ans = (ans % m * (A-i) % m * bin_exp(i+1,m-2,m) % m) % m
        
        ans = 0
        for j in range(2,A+1):
            ans = (ans % m + (ncr_mod(A,j,m) % m * j % m * (j-1) % m * bin_exp(2,j-2,m) % m)) % m
        
        return ans
            
            
                
        # return (A % m * (A-1) % m * bin_exp(3,A-2,m)) % m
