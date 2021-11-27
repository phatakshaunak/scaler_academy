'''Q2. Subset
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a set of distinct integers, A, return all possible subsets.

NOTE:

Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Also, the subsets should be sorted in ascending ( lexicographic ) order.
The list is not necessarily sorted.


Problem Constraints

1 <= |A| <= 16
INTMIN <= A[i] <= INTMAX


Input Format

First and only argument of input contains a single integer array A.



Output Format

Return a vector of vectors denoting the answer.



Example Input

Input 1:

A = [1]
Input 2:

A = [1, 2, 3]


Example Output

Output 1:

[
    []
    [1]
]
Output 2:

[
 []
 [1]
 [1, 2]
 [1, 2, 3]
 [1, 3]
 [2]
 [2, 3]
 [3]
]


Example Explanation

Explanation 1:

 You can see that these are all possible subsets.
Explanation 2:

You can see that these are all possible subsets.'''

class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def subsets(self, A):

        A.sort()
        ans, curr, idx = [], [], 0

        self.backtrack(A, curr, ans, idx)

        return ans

    def backtrack(self, A, curr, ans, idx):
        
        # When idx == len(A), we need to store the final ans, thus this condition needs to be idx > len(A)
        # if idx > len(A):
        #     return
        
        # Keep adding to answer to maintain a lexicographically sorted order of subsets
        ans.append(curr.copy())

        for i in range(idx, len(A)):
            curr.append(A[i])
            self.backtrack(A, curr, ans, i + 1)
            curr.pop()