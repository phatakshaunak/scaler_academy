'''Q3. Change character
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a string A of size N consisting of lowercase alphabets.

You can change at most B characters in the given string to any other lowercase alphabet such that the number of distinct characters in the string is minimized.

Find the minimum number of distinct characters in the resulting string.



Problem Constraints

1 <= N <= 100000

0 <= B < N



Input Format

First argument is a string A.

Second argument is an integer B.



Output Format

Return an integer denoting the minimum number of distinct characters in the string.



Example Input

A = "abcabbccd"
B = 3



Example Output

2



Example Explanation

We can change both 'a' and one 'd' into 'b'.So the new string becomes "bbcbbbccb".
So the minimum number of distinct character will be 2.'''

class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        # Initialize a frequency array
        
        freq_arr = [0] * 26
        distinct = 0
        
        # Count the total distinct elements
        
        for i in A:
            
            index = ord(i) - ord('a')
            # First occurence of an element
            
            if freq_arr[index] == 0:
                
                # First occurence, thus increment distinct
                distinct += 1
                freq_arr[index] = 1
                
            # If already present, increment count
            else:
                freq_arr[index] += 1
                
        # The goal is to minimize distinct elements, thus we can just try to reduce from lowest frequencies as long as < B. Sorting the array can help traverse the array correctly.
        
        freq_arr.sort()
        
        for j in range(len(freq_arr)):
            
            # Case when B is zero, break out of loop
            
            if B == 0:
                break
            
            # Case when frequency is <= B. This means we can reduce that element. Decrement distinct and B by the array element's frequency.
            
            if (freq_arr[j] <= B) and (freq_arr[j]  > 0):
                
                B = B - freq_arr[j]
                
                distinct -= 1
            
        return distinct
                
'''
abcabbccd

b:3
c:3
a:2
d:1

B = 3
minimize distinct characters ; start reducing the lowest counts until B is exhausted. For example, above a and d can be converted to b and c.
'''