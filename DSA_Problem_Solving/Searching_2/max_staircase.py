'''Q3. Maximum height of staircase
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an integer A representing the number of square blocks. The height of each square block is 1. The task is to create a staircase of max height using these blocks.

The first stair would require only one block, the second stair would require two blocks and so on.

Find and return the maximum height of the staircase.



Problem Constraints

0 <= A <= 109


Input Format

The only argument given is integer A.



Output Format

Return the maximum height of the staircase using these blocks.



Example Input

Input 1:

 A = 10
Input 2:

 20


Example Output

Output 1:

 4
Output 2:

 5


Example Explanation'''

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        '''The sum of steps can be represented as sum of N natural numbers
        We can apply a binary search on the max number of natural numbers equalling this sum
        i.e. x*(x+1)/2 = N...find the maximum x
        Search between 1 and N and apply binary search to get to a max value <= N
        '''

        s, e = 1, A
        ans = 0
        while s <= e:
            mid = s + (e - s) // 2

            if mid * (mid + 1) // 2 <= A:
                # Find if a larger mid is possible
                ans = mid
                s = mid + 1
            
            else:
                e = mid - 1
        
        return ans