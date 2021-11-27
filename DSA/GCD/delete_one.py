'''Q2. Delete one
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an integer array A of size N. You have to delete one element such that the GCD(Greatest common divisor) of the remaining array is maximum.

Find the maximum value of GCD.



Problem Constraints

2 <= N <= 105
1 <= A[i] <= 109



Input Format

First argument is an integer array A.



Output Format

Return an integer denoting the maximum value of GCD.



Example Input

Input 1:

 A = [12, 15, 18]
Input 2:

 A = [5, 15, 30]


Example Output

Output 1:

 6
Output 2:

 15


Example Explanation

Explanation 1:

 
 If you delete 12, gcd will be 3.
 If you delete 15, gcd will be 6.
 If you delete 18, gcd will 3.
 Maximum vallue of gcd is 6.
Explanation 2:

 If you delete 5, gcd will be 15.
 If you delete 15, gcd will be 5.
 If you delete 30, gcd will be 5.'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        def gcd(a,b):
            while a > 0 and b > 0:
                if a >= b:
                    a = a % b
                else:
                    b = b % a
            if a == 0:
                return b
            else:
                return a
        
        N = len(A)
        
        pre, suff = [0]*(N+1), [0]*(N+1)
        
        for i in range(N):
            
            pre[i+1] = gcd(pre[i],A[i])
            
            suff[N-i-1] = gcd(suff[N-i],A[N-i-1])
        
        max_val = -1
        
        for i in range(N):
            
            curr_gcd = gcd(pre[i], suff[i+1])
            max_val = max(curr_gcd, max_val)
        
        return max_val

'''
GCD does not have an inverse function to remove the contribution of one element. Thus computing the array gcd and removing each elements contribution won't work. Instead prefix and suffix GCD arrays can be used to calculate overall 
gcd when an element is removed, i.e calculate gcd(prefix[i-1], suffix[i+1]) for array element A[i], i.e. removing A[i]. Calculating prefix and suffix gcd arrays take O(Nlog(max(A)) time while traversing the array to find max GCD 
also takes O(Nlog(max(A)) time. Thus TC: O(Nlog(max(A))).
SC: O(N) for the two prefix and suffix GCD arrays
'''