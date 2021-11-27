'''Q3. Combination Sum
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a set of candidate numbers A and a target number B, find all unique combinations in A where the candidate numbers sums to B.

The same repeated number may be chosen from A unlimited number of times.

Note:

1) All numbers (including target) will be positive integers.

2) Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).

3) The combinations themselves must be sorted in ascending order.

4) CombinationA > CombinationB iff (a1 > b1) OR (a1 = b1 AND a2 > b2) OR ... (a1 = b1 AND a2 = b2 AND ... ai = bi AND ai+1 > bi+1)

5) The solution set must not contain duplicate combinations.



Problem Constraints

1 <= |A| <= 20

1 <= A[i] <= 50

1 <= B <= 500



Input Format

First argument is the vector A.

Second argument is the integer B.



Output Format

Return a vector of all combinations that sum up to B.



Example Input

Input 1:

A = [2, 3]
B = 2
Input 2:

A = [2, 3, 6, 7]
B = 7


Example Output

Output 1:

[ [2] ]
Output 2:

[ [2, 2, 3] , [7] ]


Example Explanation

Explanation 1:

All possible combinations are listed.
Explanation 2:

All possible combinations are listed.'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        # Sort the array to maintain ascending order of combinations
        A.sort()
        comb, ans, curr = [], [], [0]
        self.backtrack(A, B, 0, curr, comb, ans)
        return ans
        
    def backtrack(self, A, B, idx, curr, comb, ans):
        
        if curr[0] == B:
            ans.append(comb.copy())
            return
        
        if curr[0] > B:
            return
        
        for i in range(idx, len(A)):
            
            # Condition to avoid duplicates
            if i == 0 or A[i] != A[i-1]: 
                # Do
                comb.append(A[i])
                curr[0] += A[i]
                idx = i
                # Recur (Maintain the same index as it can be chosen multiple times)
                self.backtrack(A, B, idx, curr, comb, ans)
                # Undo
                comb.pop()
                curr[0] -= A[i]

