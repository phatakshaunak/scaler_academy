'''Q2. Lucky Numbers
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

A lucky number is a number which has exactly 2 distinct prime divisors.

You are given a number A and you need to determine the count of lucky numbers between the range 1 to A (both inclusive).



Problem Constraints

1 <= A <= 50000



Input Format

The first and only argument is an integer A.



Output Format

Return an integer i.e the count of lucky numbers between 1 and A, both inclusive.



Example Input

Input 1:

 A = 8
Input 2:

 A = 12


Example Output

Output 1:

 1
Output 2:

 3


Example Explanation

Explanation 1:

 Between [1, 8] there is only 1 lucky number i.e 6.
 6 has 2 distinct prime factors i.e 2 and 3.
Explanation 2:

 Between [1, 12] there are 3 lucky number: 6, 10 and 12.'''

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        
        ans = [0]* (A + 1)

        for i in range(2, A+1):
            if ans[i] == 0:
                ans[i] = 1
                
                for j in range(2*i, A+1, i):
                    ans[j] += 1
        
        count = 0
        for v in range(2, A+1):
            if ans[v] == 2:
                count += 1
        
        return count
