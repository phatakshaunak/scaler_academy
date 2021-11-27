'''Q4. Check two bracket expressions
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given two strings A and B. Each string represents an expression consisting of lowercase english alphabets, '+', '-', '(' and ')'.

The task is to compare them and check if they are similar. If they are similar return 1 else return 0.

NOTE: It may be assumed that there are at most 26 operands from ‘a’ to ‘z’ and every operand appears only once.



Problem Constraints

1 <= length of the each String <= 100



Input Format

The arguments given are string A and String B.



Output Format

Return 1 if they represent the same expression else return 0.



Example Input

Input 1:

 A = "-(a+b+c)"
 B = "-a-b-c"
Input 2:

 A = "a-b-(c-d)"
 B = "a-b-c-d"


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

 The expression "-(a+b+c)" can be written as "-a-b-c" which is equal as B. 
Explanation 2:

 Both the expression are different.'''

 class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        
        return 1 if self.eval_exp(A) == self.eval_exp(B) else 0
        
    def eval_exp(self, expr):
    
        seen, st = [None] * 26, []
        n = len(expr)

        for i in range(n):

            if expr[i] == '(':

                if i == 0 or expr[i-1] == '+':
                    
                    if (st and st[-1]) or (not st):
                        st.append(True)
                    else:
                        st.append(False)

                elif expr[i-1] == '-':
                    
                    if (st and not st[-1]):
                        st.append(True)
                    else:
                        st.append(False)

            elif st and expr[i] == ')':
                st.pop()

            if 97 <= ord(expr[i]) <= 122:
                
                if st:
                    l, g = self.local_sign(expr, st, i), st[-1]

                    # Sign becomes positive if both positive or negative
                    if (l == False and g == False) or (l == True and g == True):
                        seen[ord(expr[i]) - ord('a')] = True
                    # Else sign is negative
                    else:
                        seen[ord(expr[i]) - ord('a')] = False

                else:
                    # If nothing on stack, no global sign, use local sign
                    seen[ord(expr[i]) - ord('a')] = self.local_sign(expr, st, i)

        return seen
    
    def local_sign(self, s, st, idx):

        if idx == 0 or s[idx-1] == '(':
            # Positive Sign
            return True

        # Negative sign if condition return False, else positive
        else:
            return s[idx-1] == '+'

            # if s[idx-1] == '+':
            #     return True
            # if s[idx - 1] == '-':
            #     return False