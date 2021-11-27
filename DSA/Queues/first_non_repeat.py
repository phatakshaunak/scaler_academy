'''Q3. First non-repeating character
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a string A denoting a stream of lowercase alphabets.

You have to make new string B. B is formed such that we have to find first non-repeating character each time a character is inserted to the stream and append it at the end to B. if no non-repeating character is found then append '#' at the end of B.



Problem Constraints

1 <= |A| <= 100000



Input Format

The only argument given is string A.



Output Format

Return a string B after processing the stream of lowercase alphabets A.



Example Input

Input 1:

 A = "abadbc"
Input 2:

 A = "abcabc"


Example Output

Output 1:

"aabbdd"
Output 2:

"aaabc#"


Example Explanation

Explanation 1:

"a"      -   first non repeating character 'a'
"ab"     -   first non repeating character 'a'
"aba"    -   first non repeating character 'b'
"abad"   -   first non repeating character 'b'
"abadb"  -   first non repeating character 'd'
"abadbc" -   first non repeating character 'd'
Explanation 2:

"a"      -   first non repeating character 'a'
"ab"     -   first non repeating character 'a'
"abc"    -   first non repeating character 'a'
"abca"   -   first non repeating character 'b'
"abcab"  -   first non repeating character 'c'
"abcabc" -   no non repeating character so '#''''

from collections import deque

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):

        hm = {}
        q = deque()
        ans = ''

        for char in A:
            
            if char not in hm:
                hm[char] = 1
        
            else:
                hm[char] += 1

            if hm[char] == 1:
                q.append(char)

            while q and hm[q[0]] > 1:
                q.popleft()
                
            if q:
                ans = ans + q[0]
            
            else:
                ans = ans + '#'
        
        return ans

        '''
        jyhrcwuengcbnuchctluxjgtxqtfvrebveewgasluuwooupcyxwgl

        {j, y, h, r, c, w, u, e, n, g, c, b,}

        j
        '''
        # abadbc

        # seen = {}
        # b,d,

        # a, a, b, b, 
