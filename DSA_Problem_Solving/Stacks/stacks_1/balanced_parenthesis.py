'''Q1. Balanced Paranthesis
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an expression string A, examine whether the pairs and the orders of “{“,”}”, ”(“,”)”, ”[“,”]” are correct in A.

Refer to the examples for more clarity.



Problem Constraints

1 <= |A| <= 100



Input Format

The first and the only argument of input contains the string A having the paranthesis sequence.



Output Format

Return 0, if the paranthesis sequence is not balanced.

Return 1, if the paranthesis sequence is balanced.



Example Input

Input 1:

 A = {([])}
Input 2:

 A = (){
Input 3:

 A = ()[] 


Example Output

Output 1:

 1 
Output 2:

 0 
Output 3:

 1 


Example Explanation

You can clearly see that the first and third case contain valid paranthesis.

In the second case, there is no closing bracket for {, thus the paranthesis sequence is invalid.'''

class Solution:
	# @param A : string
	# @return an integer
	def solve(self, A):

        mapping = {')': '(', '}':'{', ']': '['}

        st = []

        for s in A:

            if s == '{' or s == '[' or s == '(':
                st.append(s)
            
            else:
                if not st:
                    # Empty stack ; return false as no matching opening brace
                    return 0

                elif st[-1] == mapping[s]:
                # elif (st[-1] == '(' and s == ')') or (st[-1] == '{' and s == '}') or (st[-1] == '[' and s == ']') :
                
                # If matching brace, pop from st
                    st.pop()
                
                else:
                    # Return False (as opening and close won't match)
                    return 0
        
        if st:
            return 0
        
        return 1