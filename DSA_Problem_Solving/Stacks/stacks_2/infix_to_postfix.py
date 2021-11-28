'''Q1. Infix to Postfix
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given string A denoting an infix expression. Convert the infix expression into postfix expression.

String A consists of ^, /, *, +, -, (, ) and lowercase english alphabets where lowercase english alphabets are operands and ^, /, *, +, - are operators.

Find and return the postfix expression of A.

note:

^ has highest precedence.
/ and * have equal precedence but greater than + and -.
+ and - have equal precedence and lowest precedence among given operators.


Problem Constraints

1 <= length of the string <= 500000



Input Format

The only argument given is string A.



Output Format

Return a string denoting the postfix conversion of A.



Example Input

Input 1:

 A = "x^y/(a*z)+b"
Input 2:

 A = "a+b*(c^d-e)^(f+g*h)-i"


Example Output

Output 1:

 "xy^az*/b+"
Output 2:

 "abcd^e-fgh*+^*+i-"


Example Explanation

Explanation 1:

 Ouput dentotes the postfix expression of the given input.'''

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):

        st = []
        order = {'+' : 1, '-' : 1, '*': 2, '/': 2, '^': 3}

        ans = ''

        for char in A:

            if char in order:

                while st and st[-1] in order and order[st[-1]] >= order[char]:
                    ans = ans + st.pop()

            # elif char not in order and char != '(' and char != ')':

            # Add lower case alphabets to the answer
            if 97 <= ord(char) <= 122:
                ans = ans + char

            elif char == ')':
                while st and st[-1] != '(':
                    ans = ans + st.pop()

                st.pop()

                # # To avoid appending ')' to the answer
                # continue
            
            # Append operator or opening braces to the stack
            if not 97 <= ord(char) <= 122 and char != ')':
                st.append(char)
        
        while st:
            ans = ans + st.pop()
        
        return ans
            

