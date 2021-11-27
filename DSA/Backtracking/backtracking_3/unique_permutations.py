'''Q4. All Unique Permutations
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array A of size N denoting collection of numbers that might contain duplicates, return all possible unique permutations.

NOTE: No 2 entries in the permutation sequence should be the same.

WARNING: DO NOT USE LIBRARY FUNCTION FOR GENERATING PERMUTATIONS. Example : next_permutations in C++ / itertools.permutations in python.
If you do, we will disqualify your submission retroactively and give you penalty points.


Problem Constraints

1 <= |A| <= 9

0 <= A[i] <= 10



Input Format

Only argument is an integer array A of size N.



Output Format

Return a 2-D array denoting all possible unique permutation of the array.



Example Input

Input 1:

A = [1, 1, 2]
Input 2:

A = [1, 2]


Example Output

Output 1:

[ [1,1,2]
  [1,2,1]
  [2,1,1] ]
Output 2:

[ [1, 2]
  [2, 1] ]


Example Explanation

Explanation 1:

 All the possible unique permutation of array [1, 1, 2].
Explanation 2:

 All the possible unique permutation of array [1, 2].'''

class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def permute(self, A):

        hm = {}
        for val in A:
            if val not in hm:
                hm[val] = 1
            else:
                hm[val] += 1

        curr, ans = [], []

        self.dfs(A, curr, ans, hm)

        return ans
        
    def dfs(self, A, curr, ans, hm):

        if len(curr) == len(A):
            ans.append(curr.copy())
            return
        
        for val in hm:
            if hm[val] > 0:
                curr.append(val)
                hm[val] -= 1
                self.dfs(A, curr, ans, hm)
                curr.pop()
                hm[val] += 1