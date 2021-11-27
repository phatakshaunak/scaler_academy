'''Q3. Make String Pallindrome
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a string A of size N consisting only of lowercase alphabets. The only operation allowed is to insert characters in the beginning of the string.

Find and return how many minimum characters are needed to be inserted to make the string a palindrome string.



Problem Constraints

1 <= N <= 106



Input Format

The only argument given is a string A.



Output Format

Return an integer denoting the minimum characters that are needed to be inserted to make the string a palindrome string.



Example Input

Input 1:

 A = "abc"
Input 2:

 A = "bb"


Example Output

Output 1:

 2
Output 2:

 0


Example Explanation

Explanation 1:

 Insert 'b' at beginning, string becomes: "babc".
 Insert 'c' at beginning, string becomes: "cbabc".
Explanation 2:

 There is no need to insert any character at the beginning as the string is already a palindrome.'''

class Solution:
	# @param A : string
	# @return an integer
	def solve(self, A):
        
        '''Create a Z-array and check for the condition N - i == Z[i]
           We are trying to find the largest palindrome possible in the given string ; this will be a substring which matches some characters from the front
           i.e. find out the largest suffix (reversed) that is also equal to the prefix. This will be a palindrome. Then the remaining characters need to be appended
           to the front to make the whole string a palindrome, i.e len(string) - Z[i]
        '''
        
        pattern = A + '$'
        for i in range(len(A)-1,-1,-1):
            pattern = pattern + A[i]
        
        N = len(pattern)

        z_arr = self.generate_z(pattern)

        for k in range(len(A)+1, N):

            if z_arr[k] == N - k:
                return len(A) - z_arr[k]
        
    def generate_z(self, st):
        
        n = len(st)
        Z = [0 for idx in range(n)]
        Z[0] = n
        
        L, R = 0, 0

        for i in range(1, n):

            # Outside box
            if i > R:
                # Resize the box
                L, R = i, i
                # Run loop to find longest suffix equal to prefix
                while R < n and st[R] == st[R - L]:
                    # Expand box
                    R += 1
                # Reduce R by 1 as outside valid prefix
                R -= 1
                # Update Z[i]
                Z[i] = R - L + 1
            
            # Inside box
            else:
                # Prefix value within the box (i.e can simply copy previous prefix)
                j = i - L
                if Z[j] < R - i + 1:
                    # Copy answer from Z[j]
                    Z[i] = Z[j]
                # At the edge or out of box
                else:
                    # Resize box
                    L = i
                    # Same code as when i > R
                    while R < n and st[R] == st[R - L]:
                        # Expand box
                        R += 1
                    # Reduce R by 1 as outside valid prefix
                    R -= 1
                    # Update Z[i]
                    Z[i] = R - L + 1

        return Z