'''Q5. Min Sum Path in Triangle
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

Adjacent numbers for jth number of row i is jth and (j+1)th numbers of row i+1 is



Problem Constraints

|A| <= 1000

A[i] <= 1000



Input Format

First and only argument is the vector of vector A defining the given triangle



Output Format

Return the minimum sum



Example Input

Input 1:

 
A = [ 
         [2],
        [3, 4],
       [6, 5, 7],
      [4, 1, 8, 3]
    ]
Input 2:

 A = [ [1] ]


Example Output

Output 1:

 11
Output 2:

 1


Example Explanation

Explanation 1:

 The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
Explanation 2:

 Only 2 can be collected.'''

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):

        return self.min_path_space(A)
    
    def min_path_space(self, arr):
    
        if len(arr) == 1:
            return min(arr[0])
        
        dp1 = [None for i in range(len(arr[-1]))]
        dp2 = dp1.copy()
        
        dp1[0] = arr[0][0]
        ans = float('inf')

        for i in range(1, len(arr)):
            
            for j in range(len(arr[i])):
                
                if j == 0:
                    dp2[j] = arr[i][j] + dp1[j]
                
                else:
                    tmp = float('inf')
                    
                    if dp1[j] != None:
                        tmp = min(tmp, arr[i][j] + dp1[j])
                    
                    if dp1[j-1] != None:
                        tmp = min(tmp, arr[i][j] + dp1[j - 1])
                    
                    dp2[j] = tmp
            
                if i == len(arr) - 1:
                    ans = min(ans, dp2[j])
            
            dp1, dp2 = dp2, dp1
        
        return ans
            
    def min_path_t(self, a):
    
        if len(a) == 1:
            return min(a[0])
            
        dp = [[None for i in range(len(a[-1]))] for j in range(len(a))]
        
        dp[0][0] = a[0][0]
        ans = float('inf')
        for i in range(1, len(a)):
            
            for j in range(len(a[i])):
                
                if j == 0:
                    dp[i][j] = a[i][j] + dp[i - 1][j]
                
                else:
                    tmp = float('inf')

                    if dp[i - 1][j] != None:
                        
                        tmp = min(tmp, a[i][j] + dp[i - 1][j])

                    if dp[i - 1][j - 1] != None:

                        tmp = min(tmp, a[i][j] + dp[i - 1][j - 1])

                    dp[i][j] = tmp
                
                if i == len(a) - 1:
                    ans = min(ans, dp[i][j])
        
        return ans