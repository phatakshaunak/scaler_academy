'''Q3. Longest Balanced Substring
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a string A made up of multiple brackets of type "[]" , "()" and "{}" find the length of the longest substring which forms a balanced string .

Conditions for a string to be balanced :

Blank string is balanced ( However blank string will not be provided as a test case ).
If B is balanced : (B) , [B] and {B} are also balanced.
If B1 and B2 are balanced then B1B2 i.e the string formed by concatenating B1 and B2 is also balanced.


Problem Constraints

0 <= |A| <= 106



Input Format

First and only argument is an string A.



Output Format

Return an single integer denoting the lenght of the longest balanced substring.



Example Input

Input 1:

 A = "[()]"
Input 2:

 A = "[(])"


Example Output

Output 1:

 4
Output 2:

 0


Example Explanation

Explanation 1:

 Substring [1:4] i.e "[()]" is the longest balanced substring of length 4.
Explanation 2:

 None of the substring is balanced so answer is 0.'''

class Solution:
    # @param A : string
    # @return an integer
    def LBSlength(self, A):
        
        '''
        Use an array to store answer ending at index i
        If an opening bracket is encountered, no substring ending at i is balanced
        If closing is encountered, 
            Case 1 if it's previous is an opening, add 2 + dp[i - 2]
            Case 2 If the previous is also a closing, find the possible start index for the substring
            Check if it is a corresponding opening bracket for the closing at A[i], then simply add 2 + dp[start - 1]
            + dp[i - 1] if start >= 0, else simply add 2 + dp[start - 1]
        '''
        
        mapping = {')': '(', '}': '{', ']': '['}
        
        n = len(A)
        
        dp = [0 for i in range(n)]
        ans = 0
        for i in range(n):
            
            if A[i] in mapping:
                # Closing bracket encountered
                
                # Case 1, valid opening bracket found
                if i > 0 and mapping[A[i]] == A[i - 1]:
                    if i - 2 >= 0:
                        dp[i] = dp[i] + 2 + dp[i - 2]
                    else:
                        dp[i] = dp[i] + 2
                
                # Case 2, another closing bracket found
                if i > 0 and A[i - 1] in mapping:
                    # Get start index for possible opening bracket matching A[i]
                    start = i - 1 - dp[i - 1]
                    
                    if start >= 0:
                        # Opening and closing brackets match
                        if A[start] == mapping[A[i]]:
                            # Add previous answer if valid index
                            if start - 1 >= 0:
                                dp[i] = dp[i] + dp[i - 1] + 2 + dp[start - 1]
                            else:
                                dp[i] = dp[i] + dp[i - 1] + 2
            
            ans = max(ans, dp[i])
        
        return ans
    
    # Stack solution: Reference: https://leetcode.com/problems/longest-valid-parentheses/discuss/1139974/PythonGo-O(n)-by-stack-w-Comment