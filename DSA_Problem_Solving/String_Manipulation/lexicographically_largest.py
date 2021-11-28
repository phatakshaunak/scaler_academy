'''Q7. Lexicographically Largest
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
You are given a string S. You want to change it to the lexicographically largest possible string by changing some of its characters. But you can only use characters of the string T as a replacement for characters of S. Formally, find the lexicographically largest string you can form by replacing some(or none) of the characters of S by using only the characters of string T. Note: Each character of T can be used at the most once.

Constraints:

1.   1 <= Length of S and T <= 50
2.   All the alphabets of S and T are lower case (a - z)
Input: A string A containing S and T separated by "_" character. (See example below)

Output: Lexicographically largest string P that can be formed by changing some or (none) characters of S using the characters of T.

Example:

Input:

A : "abb_c"
This implies S is "abb" and T is "c".

Output:

P = "cbb"'''

class Solution:
    # @param A : string
    # @return a strings
    def getLargest(self, A):
        
        l_max = ''
        
        T = []
        t_bool = False
        
        for i in range(len(A)):
            
            if A[i] == '_':
                
                s_ind = i
                t_bool = True
            
            if t_bool == True and i > s_ind:
                T.append(A[i])
        
        T = sorted(T,reverse=True)
        
        N = len(T)
        
        t = 0
        
        for i in range(s_ind):
            
            # Case when the T string has been consumed
            if t > (N-1):
                l_max += A[i]
            
            # Case when T string's character greater than s, replace with T's character, increment T's index as we can use only once.
            elif A[i] < T[t]:
                l_max += T[t]
                t += 1
            # Case when S's character is greater than equal to that of T, then append S's character and do not change T's index.
            else:
                l_max += A[i]
            
        return l_max