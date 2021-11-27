'''Q4. Pair Sum divisible by M
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of integers A and an integer B, find and return the number of pairs in A whose sum is divisible by B.

Since the answer may be large, return the answer modulo (109 + 7).



Problem Constraints

1 <= length of the array <= 100000
1 <= A[i] <= 109
1 <= B <= 106



Input Format

The first argument given is the integer array A.
The second argument given is the integer B.



Output Format

Return the total number of pairs for which the sum is divisible by B modulo (109 + 7).



Example Input

Input 1:

 A = [1, 2, 3, 4, 5]
 B = 2
Input 2:

 A = [5, 17, 100, 11]
 B = 28


Example Output

Output 1:

 4
Output 2:

 1


Example Explanation

Explanation 1:

 All pairs which are divisible by 2 are (1,3), (1,5), (2,4), (3,5). 
 So total 4 pairs.'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        hm = {}
        pair = 0
        for i in range(len(A)):
            A[i] = A[i] % B
        
        for j in range(len(A)):
            if ((B - A[j]) in hm) and A[j] != 0:
                pair += hm[B-A[j]]
            
            elif A[j] == 0:
                if A[j] in hm:
                    pair += hm[A[j]]
        
            if A[j] in hm:
                hm[A[j]] += 1
            else:
                hm[A[j]] = 1
        
        return pair % int(1e9+7)

'''
[1 2 3 4 5] M = 2
mod 2 [1 0 1 0 1]
{0:2, 1:3}

mod 3 [1 0 1 0 1]
pair sum % M = 0
{1:1
 0:2
count += hm[i]   4
5 17 100 11 28
5 17 16 11
22 21 16 33 28 27
(A+C) % M = M % M = 0
(A%M +C%M) = M
two cases: A%M and C%M are non zero ; or both are zeros
17 % 4 = 2
{
'''