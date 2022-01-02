'''Q1. Simplify Directory Path
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Given a string A representing an absolute path for a file (Unix-style).

Return the string A after simplifying the absolute path.

Note:

Absolute path always begin with '/' ( root directory ).

Path will not have whitespace characters.


Input Format

The only argument given is string A.
Output Format

Return a string denoting the simplified absolue path for a file (Unix-style).
For Example

Input 1:
    A = "/home/"
Output 1:
    "/home"

Input 2:
    A = "/a/./b/../../c/"
Output 2:
    "/c"'''

class Solution:
	# @param A : string
	# @return a strings
	def simplifyPath(self, A):

        i, n = 0, len(A)
        st = []
        curr = ''
    
        while i < n:

            # if A[i].isalpha():
            if 67 <= ord(A[i]) <= 122:
                # Accumulate folder name and push to stack
                while i < n and A[i].isalpha():
                    curr += A[i]
                    i += 1
                i -= 1
                st.append(curr)
                curr = ''
            
            elif A[i] == '.':
                
                # Pop from stack if next element is also a '.'
                if st and i + 1 < n and A[i + 1] == '.':
                    st.pop()

                # Do nothing if a single '.' as that implies current directory
            
            i += 1
        
        return '/' + '/'.join(st)

        # Solution may become easier by using the inbuilt split function