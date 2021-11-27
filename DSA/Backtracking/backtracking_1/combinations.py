'''Q3. Combinations
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given two integers A and B, return all possible combinations of B numbers out of 1 2 3 … A .

Make sure the combinations are sorted.

To elaborate,

Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
Entries should be sorted within themselves.
WARNING: DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.



Problem Constraints

1 <= A, B <= 10



Input Format

First argument is an integer A.
Second argument is an integer B.



Output Format

Return a 2-D vector denoting all possible combinations.



Example Input

Input 1:

 A = 4
 B = 2
Input 2:

 A = 3
 B = 2


Example Output

Output 1:

 [
  [1, 2],
  [1, 3],
  [1, 4],
  [2, 3],
  [2, 4],
  [3, 4],
 ]
Output 2:

 [
  [1, 2],
  [1, 3],
  [2, 3]
 ] 


Example Explanation

Explanation 1:

All the possible combinations of size 2 in sorted order.'''

class Solution:
	# @param A : integer
	# @param B : integer
	# @return a list of list of integers
	def combine(self, A, B):

        ans, curr = [], []

        self.backtrack(A, B, curr, ans, 1)

        return ans

    def backtrack(self, A, B, curr, ans, idx):

        # Base Case
        if len(curr) == B:
            ans.append(curr.copy())
            return
        
        for i in range(idx, A + 1):
            curr.append(i)
            self.backtrack(A, B, curr, ans, i + 1)
            curr.pop()