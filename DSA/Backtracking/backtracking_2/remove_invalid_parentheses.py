'''Q1. Remove Invalid Parentheses
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a string A consisting of lowercase English alphabets and parentheses '(' and ')'. Remove the minimum number of invalid parentheses in order to make the input string valid.

Return all possible results.

You can return the results in any order.



Problem Constraints

1 <= length of the string <= 20



Input Format

The only argument given is string A.



Output Format

Return all possible strings after removing the minimum number of invalid parentheses.



Example Input

Input 1:

 A = "()())()"
Input 2:

 A = "(a)())()"


Example Output

Output 1:

 ["()()()", "(())()"]
Output 2:

 ["(a)()()", "(a())()"]


Example Explanation

Explanation 1:

 By removing 1 parentheses we can make the string valid.
        1. Remove the parentheses at index 4 then string becomes : "()()()"
        2. Remove the parentheses at index 2 then string becomes : "(())()"
Explanation 2:

 By removing 1 parentheses we can make the string valid.
        1. Remove the parentheses at index 5 then string becomes : "(a)()()"
        2. Remove the parentheses at index 2 then string becomes : "(a())()"'''

class Solution:
    # @param A : string
    # @return a list of strings
    def solve(self, A):
    
        #All possible removals (should be len(A) - 2 as minimum valid condition should be () ?)
        ans = [[] for i in range(len(A))]

        #Temp list to store candidate ans
        curr = []
        
        look_up = set() o

        self.backtrack(A, 0, curr, ans, look_up)
        
        for a in ans:
            if len(a) != 0:
                return a
        
        #If no valid answer
        return ['']
    
    def backtrack(self, A, idx, curr, ans, look_up):
        
        # Base cases
        
        if idx == len(A):
            
            if self.valid_parens(curr) and ''.join(curr) not in look_up:
                
                # Calculate min removals by difference of lengths
                pos = len(A) - len(curr)
                ans[pos].append(''.join(curr))
                look_up.add(''.join(curr))
                return
            
            else:
                return
        
        if A[idx] != '(' and A[idx] != ')':
            curr.append(A[idx])
            self.backtrack(A, idx + 1, curr, ans, look_up)
            curr.pop()
            
        else:
            curr.append(A[idx])
            self.backtrack(A, idx + 1, curr, ans, look_up)
            curr.pop()
            
            self.backtrack(A, idx + 1, curr, ans, look_up)

    def valid_parens(self, s):
        
        l, r = 0, 0
        # Empty string
        if not s:
            return False

        stack = []
        for char in s:
            if char != '(' and char != ')':
                continue # skip alphabets as they don't determine valid parentheses

            elif char == '(':
                l += 1
                stack.append(char)
            elif char == ')':
                r += 1
                if not stack: # Empty stack, no matching open brackets
                    return False
                else:
                    stack.pop()
        
        #If only alphabets in the string, l and r both should be zero
        # if l == 0 and r == 0:
        #     return False
        
        #If stack empty, valid string
        if not stack: # Empty stack, matching all parentheses
            return True

        return False

