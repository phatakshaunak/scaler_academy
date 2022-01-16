'''Q2. Unique Binary Search Trees II
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an integer A, how many structurally unique BST's (binary search trees) exist that can store values 1…A?



Problem Constraints

1 <= A <=18



Input Format

First and only argument is the integer A



Output Format

Return a single integer, the answer to the problem



Example Input

Input 1:

 1
Input 2:

 2


Example Output

Output 1:

 1
Output 2:

 2


Example Explanation

Explanation 1:

 Only single node tree is possible.
Explanation 2:

 2 trees are possible, one rooted at 1 and other rooted at 2.'''

class Solution:
	# @param A : integer
	# @return an integer
	def numTrees(self, A):

        # memo = [-1 for i in range(A + 1)]

        # return self.ways_bst_rec(A, memo)

        # return self.ways_bst_tab(A)

        return self.ways_bst_catalan(A)

    # TC: O(N^2), SC: O(N)
    def ways_bst_rec(self, N, memo):
    
        if N == 0:
            if memo[N] == -1:
                memo[N] = 1
            return memo[N]
        
        if memo[N] == -1:
            
            memo[N] = 0
            for x in range(1, N + 1):
                
                memo[N] += (self.ways_bst_rec(x - 1, memo) * self.ways_bst_rec(N - x, memo))
        
        return memo[N]

    # TC: O(N^2), SC: O(N)
    def ways_bst_tab(self, N):
    
        dp = [0 for i in range(N + 1)]
        
        dp[0] = 1
        
        # Iterate over dp state
        for i in range(1, N + 1):
        
            # Iterate over all possible values for the root node
            for j in range(1, i + 1):
                
                # Calculate answers for state i of the dp table
                dp[i] = dp[i] + (dp[j - 1] * dp[i - j])
        
        return dp[N]
    
    # Based on the calculation of Catalan Numbers, O(N) time, O(1) space
    def ways_bst_catalan(self, N):

        num, den = 1, 1

        idx = 1
        tmp = 2 * N
        while idx <= N:

            num = num * tmp
            den = den * idx

            tmp -= 1
            idx += 1
        
        ans = (num // den) // (N + 1)

        return an