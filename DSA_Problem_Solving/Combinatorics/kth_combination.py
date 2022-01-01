'''Q1. Kth Permutation Sequence
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, We get the following sequence (ie, for n = 3 ) :

1. "123"
2. "132"
3. "213"
4. "231"
5. "312"
6. "321"
Given n and k, return the kth permutation sequence.

For example, given n = 3, k = 4, ans = "231"

Good questions to ask the interviewer :

What if n is greater than 10. How should multiple digit numbers be represented in string?
In this case, just concatenate the number to the answer. so if n = 11, k = 1, ans = "1234567891011"

Whats the maximum value of n and k?
In this case, k will be a positive integer thats less than INT_MAX. n is reasonable enough to make sure the answer does not bloat up a lot.'''

class Solution:
	# @param A : integer
	# @param B : integer
	# @return a strings
	def getPermutation(self, A, B):

        return self.perm_seq(A, B)

        # curr, ans, seen = [], [], set()

        # K = [B]

        # self.dfs_perm(A, ans, curr, 1, seen, K)

        # return ans[0]

    # Backtracking solution O(N*N!)
    def dfs_perm(self, N, ans, curr, idx, seen, K):
    
        if len(curr) == N:
            K[0] = K[0] - 1
            
            # Add to answer when Kth permutation is reached
            if not K[0]:
                ans.append(''.join([str(i) for i in curr]))
            return
        
        for i in range(1, N + 1):

            # Recur only when i not added to set or K is non-zero
            if i not in seen and K[0]:
                curr.append(i)
                seen.add(i)
                self.dfs_perm(N, ans, curr, i + 1, seen, K)
                curr.pop()
                seen.remove(i)

    # Mathematical observation based solution O(N^2)
    def fact(self, num):
        ans = 1
        while num:
            ans = ans * num
            num -= 1
        return ans

    def perm_seq(self, N, K):
        
        nums = [str(i) for i in range(1, N + 1)]
        # Generate 0 to N-1!
        factorial = [self.fact(i) for i in range(N)]
        
        ans = ''
        
        while N:
            # Digit to insert
            idx = K // factorial[N-1]
            
            # Edge case when at the boundary of a block, decrement index
            if K % factorial[N-1] == 0:
                idx -= 1
            
            # print(idx, nums, K)
            
            ans = ans + nums[idx]
            
            # Remove number
            nums.pop(idx)
            
            # Update N and K
            K = K - idx * factorial[N-1]
            N -= 1
        
        return ans

    # Reference: https://www.youtube.com/watch?v=W9SIlE2jhBQ