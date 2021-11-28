'''Q3. Count of divisors
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of integers A, find and return the count of divisors of each element of the array.

NOTE: Order of the resultant array should be same as the input array.



Problem Constraints

1 <= length of the array <= 100000
1 <= A[i] <= 106



Input Format

The only argument given is the integer array A.



Output Format

Return the count of divisors of each element of the array in the form of an array.



Example Input

Input 1:

 A = [2, 3, 4, 5]
Input 2:

 A = [8, 9, 10]


Example Output

Output 1:

 [2, 2, 3, 2]
Output 1:

 [4, 3, 4]


Example Explanation

Explanation 1:

 The number of divisors of 2 : [1, 2], 3 : [1, 3], 4 : [1, 2, 4], 5 : [1, 5]
 So the count will be [2, 2, 3, 2].
Explanation 2:

 The number of divisors of 8 : [1, 2, 4, 8], 9 : [1, 3, 9], 10 : [1, 2, 5, 10]
 So the count will be [4, 3, 4].'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        
        # Generate an SPF array from 1 to max(A) and then prime factorize each element in the array
        
        N = max(A)
        
        spf = [0] * (N+1)
        
        for i in range(2,N+1):
            
            if spf[i] == 0:
                spf[i] = i
                
                for j in range(i*i,N+1,i):
                    if spf[j] == 0:
                        spf[j] = i
        
        ans = []
        
        for val in A:
            count = 1
            while val > 1:
                prime = spf[val]
                p = 1
                while val % prime == 0:
                    p += 1
                    val = val // prime
                
                count = count * p    
                    
            ans.append(count)
        
        return ans
        
'''Formula for number of divisors is given as (p1+1)*(p2+1)*....(pm+1) where p1,p2,...pm are prime factors of the number.
   An SPF array can be generated to store factors for 1 to max value in the array.
   Then we need to find out the exponents for all the prime factors in the given number.
'''
        