'''Q3. Evaluate Expression
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

An arithmetic expression is given by a charater array A of size N. Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each character may be an integer or an operator.



Problem Constraints

1 <= N <= 105



Input Format

The only argument given is character array A.



Output Format

Return the value of arithmetic expression formed using reverse Polish Notation.



Example Input

Input 1:
    A =   ["2", "1", "+", "3", "*"]
Input 2:
    A = ["4", "13", "5", "/", "+"]


Example Output

Output 1:
    9
Output 2:
    6


Example Explanation

Explaination 1:
    starting from backside:
    * : () * ()
    3 : () * (3)
    + : (() + ()) * (3)
    1 : (() + (1)) * (3)
    2 : ((2) + (1)) * (3)
    ((2) + (1)) * (3) = 9
Explaination 2:
    + : () + ()
    / : () + (() / ())
    5 : () + (() / (5))
    1 : () + ((13) / (5))
    4 : (4) + ((13) / (5))
    (4) + ((13) / (5)) = 6'''

class Solution:
	# @param A : list of strings
	# @return an integer
	def evalRPN(self, A):
        
        ops = {'+', '/', '-', '*'}

        s = []
        for c in A:

            # If a number, push it to the stack
            if c not in ops:
                s.append(int(c))
            
            else:
                
                # Need two operands to perform an operation ; not valid postfix, thus return 0
                if len(s) < 2:
                    return 0

                a2 = s.pop()
                a1 = s.pop()

                if c == '+':
                    s.append(a1 + a2)
                
                elif c == '-':
                    s.append(a1 - a2)
                
                elif c == '/':
                    s.append(a1 // a2)
                
                else:
                    s.append(a1 * a2)
        # Need a single number after evaluation
        if len(s) == 1:
            return s.pop()

        # If not a single number return 0 as not a postfix expression
        return 0