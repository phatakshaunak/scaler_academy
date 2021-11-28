'''Q3. Window String
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a string A and a string B, find the window with minimum length in A which will contain all the characters in B in linear time complexity.
Note that when the count of a character c in B is x, then the count of c in minimum window in A should be at least x.

Note:

If there is no such window in A that covers all characters in B, return the empty string.
If there are multiple such windows, return the first occurring minimum window ( with minimum start index )


Problem Constraints

1 <= size(A), size(B) <= 106



Input Format

First argument is a string A.
Second argument is a string B.



Output Format

Return a string denoting the minimum window.



Example Input

Input 1:

 A = "ADOBECODEBANC"
 B = "ABC"
Input 2:

 A = "Aa91b"
 B = "ab"


Example Output

Output 1:

 "BANC"
Output 2:

 "a91b"


Example Explanation

Explanation 1:

 "BANC" is a substring of A which contains all characters of B.
Explanation 2:

 "a91b" is the substring of A which contains all characters of B.'''

class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
	def minWindow(self, A, B):

        hm, need, ans = {}, 0, float('inf')
        m, n  = len(A), len(B)
        l, r = -1, -1
        # Fill frequency map for B
        for char in B:
            if char not in hm:
                hm[char] = 1
            else:
                hm[char] += 1
            need += 1
        
        i = 0 # left pointer

        for j in range(m):

            #Decrement need if char in hm and frequency greater than zero
            if A[j] in hm:
                if hm[A[j]] > 0:
                    need -= 1
                # Decrement frequency
                hm[A[j]] -= 1

            # Update ans if need is zero
            if need == 0:
                if ans > (j - i + 1):
                    ans = (j - i + 1)
                    l, r = i, j
            
            # Shrink window until need stays zero
            # while need == 0 and i < m:
            while need == 0:
                # Remove ith element from window if in map, increment count in frequency map and increment need only if it's frequency is >0 (might be just == 0 instad of >= 0)

                if A[i] in hm:
                    if hm[A[i]] == 0:
                        need += 1
                    hm[A[i]] += 1

                # Shrink the window by moving i
                i += 1

                # Update ans if need is zero
                if need == 0:
                    if ans > (j - i + 1):
                        ans = (j - i + 1)
                        l, r = i, j
        
        return A[l:r+1]

        # TC O(len(A)), SC O(len(B))

        '''
            j
        ADOBECODEBANC
        i    
        ABC
        len = 6
        '''