'''Q2. Generate all Parentheses II
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an integer A pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*A.



Problem Constraints

1 <= A <= 20



Input Format

First and only argument is integer A.



Output Format

Return a sorted list of all possible paranthesis.



Example Input

Input 1:

A = 3
Input 2:

A = 1


Example Output

Output 1:

[ "((()))", "(()())", "(())()", "()(())", "()()()" ]
Output 2:

[ "()" ]


Example Explanation

Explanation 1:

 All paranthesis are given in the output list.
Explanation 2:

 All paranthesis are given in the output list.'''

class Solution:
	# @param A : integer
	# @return a list of strings
	def generateParenthesis(self, A):
	    ans, curr = [], []
	    self.valid_parens(A, ans, curr, 0, 0)
	    
	    return ans
	
	def valid_parens(self, A, ans, curr, op, cl):
	    
	    if op > A or cl > op:
	        return
	    
	    if (op == cl) and op == A:
	        ans.append(''.join(curr.copy()))
	        return
	    
	    curr.append('(')
	    op += 1
	    self.valid_parens(A, ans, curr, op, cl)
	    curr.pop()
	    op -= 1
	    
	    curr.append(')')
	    cl += 1
	    self.valid_parens(A, ans, curr, op, cl)
	    curr.pop()
	    cl -= 1
