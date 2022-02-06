'''Q2. Burst Balloons
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

You are given N balloons each with a number of coins associated with them. An array of integers A represents the coins associated with the ith balloon.
You are asked to burst all the balloons. If the you burst balloon ith you will get A[left] * A[i] * A[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

NOTE: You may imagine A[-1] = A[N] = 1. They are not real therefore you can not burst them.



Problem Constraints

1 <= N <= 100
1 <= A[i] <= 100



Input Format

The only argument given is the integer array A.



Output Format

Return the maximum coins you can collect by bursting the balloons wisely.



Example Input

Input 1:

 A = [3, 1, 5, 8]
Input 2:

 A = [3, 1, 2]


Example Output

Output 1:

 167
Output 2:

 15


Example Explanation

Explanation 1:

 Burst ballon at index 1, coins collected = 3*1*5=15 , A becomes = [3, 5, 8] 
 Burst ballon at index 1, coins collected = 3*5*8=120 , A becomes = [3, 8]
 Burst ballon at index 0, coins collected = 1*3*8=24 , A becomes = [8]
 Burst ballon at index 0, coins collected = 1*8*1 = 8
 Total coins collected = 15 + 120 + 24 + 8 = 167
Explanation 2:

 Burst ballon at index 1, coins collected = 3*1*2 = 6, A becomes = [3, 2] 
 Burst ballon at index 1, coins collected = 3*2*1 = 6, A becomes = [3]
 Burst ballon at index 0, coins collected = 1*3*1 = 3
 Total coins collected = 6 + 6 + 3 = 15'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        return self.mcm_variation(A)

    def burst_balloons_tabular(self, A):
    
        N = len(A)
        A_mod = [1 for i in range(N + 2)]
        
        for i in range(1, N + 1):
            A_mod[i] = A[i - 1]
        
        dp = [[0 for i in range(N + 2)] for j in range(N + 2)]
        
        # Try subarrays of all lengths (1 to N)
        for l in range(1, N + 1):
            
            # Fix start indices
            for st in range(1, N - l + 2):
                
                e = l + st - 1
                
                # Try all elements in each subarray as the last element to burst
                for k in range(st, e + 1):
                    
                    # Best cost of bursting left part in subarray (0 if nothing exists, padding added to the dp array, same logic for right)
                    left = dp[st][k - 1]
                    right = dp[k + 1][e]
                    
                    # Since A_mod[k] is the last to be burst, consider first values out of the subarray that remain to calculate cost to burst A, 1 if out of bounds, padding added to A_mod
                    val = A_mod[st - 1] * A_mod[k] * A_mod[e + 1]
                    
                    cost = left + right + val

                    if dp[st][e] < cost:
                        dp[st][e] = cost
        
        return dp[1][N]
    
    def mcm_variation(self, A):

        N = len(A)
        A_mod = [1 for i in range(N + 2)]
        
        for i in range(1, N + 1):
            A_mod[i] = A[i - 1]
         
        dp = [[0 for i in range(N + 2)] for j in range(N + 2)]

        for l in range(2, N + 2):

            for st in range(1, N - l + 3):

                e = l + st - 1

                if e - st + 1 == 2:

                    dp[st][e] = A_mod[st - 1] * A_mod[st] * A_mod[e]
                
                else:

                    for k in range(st, e):

                        # Left subarrays cost
                        left = dp[st][k]

                        # Right subarrays cost
                        right = dp[k + 1][e]

                        # Subsequent final 2 matrix multiplication cost
                        val = A_mod[st - 1] * A_mod[k] * A_mod[e]

                        cost = left + right + val

                        if cost > dp[st][e]:

                            dp[st][e] = cost
        
        return dp[1][-1]