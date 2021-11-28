'''Q3. Primal Power
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

"Primal Power" of an array is defined as the count of prime numbers present in it.

Given an array of integers A of length N, you have to calculate its Primal Power.



Problem Constraints

1 <= N <= 103

-106 <= A[i] <= 106



Input Format

First and only argument is an integer array A.



Output Format

Return the Primal Power of array A.



Example Input

Input 1:

 A = [-6, 10, 12]
Input 2:

 A = [-11, 7, 8, 9, 10, 11]


Example Output

Output 1:

 0
Output 2:

 2


Example Explanation

Explanation 1:

 -6 is not a prime number, as prime numbers are always natural numbers(by definition). 
  Also, both 10 and 12 are composite numbers.
Explanation 2:

 7 and 11 are prime numbers. Hence, Primal Power = 2.'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        count = 0
        def check_prime(n):
            sq = int(n**(0.5))
            for i in range(2, sq+1):
                if n % i == 0:
                    return 0
            return 1
            
        for i in A:
            if i > 1:
                count += check_prime(i)
        
        return count