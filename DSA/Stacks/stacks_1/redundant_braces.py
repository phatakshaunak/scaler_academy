'''Q2. Redundant Braces
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a string A denoting an expression. It contains the following operators '+', '-', '*', '/'.

Chech whether A has redundant braces or not.

NOTE: A will be always a valid expression.



Problem Constraints

1 <= |A| <= 105



Input Format

The only argument given is string A.



Output Format

Return 1 if A has redundant braces, else return 0.



Example Input

Input 1:

 A = "((a+b))"
Input 2:

 A = "(a+(a+b))"


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

 ((a+b)) has redundant braces so answer will be 1.
Explanation 2:

 (a+(a+b)) doesn't have have any redundant braces so answer will be 0.'''

 class Solution:
	# @param A : string
	# @return an integer
	def braces(self, A):
        
        st = []
    
        for c in A:
            if c == '(' or c in {'+','-','*','/'}:
                st.append(c)
            
            elif c == ')':
                if st and st[-1] in {'+','-','*','/'}:
                    while st and st[-1] != '(':
                        st.pop()
                    # Pop matching opening brace
                    st.pop()
                else:
                    return 1
        return 0