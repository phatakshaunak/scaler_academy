'''Q3. Perfect Cards
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Tom and Harry are given N numbers, with which they play a game as a team.

Initially, Tom chooses a particular number P from the N numbers, and he takes away all the numbers that are equal to P.

Next, Harry chooses a different number Q, different from what Tom chose, and takes away all the numbers equal to Q from the remaining N numbers.

They win the game if they can take all the numbers by doing the above operation once and if each of them has the same amount of numbers towards the end.

If they win, return the string "WIN", else return "LOSE".



Problem Constraints

2 <= N <= 100

1 <= A[i] <= 100



Input Format

The first and the only argument of input contains an integer array, A.



Output Format

Return a string, denoting the answer.



Example Input

Input 1:

 A = [1, 2]
Input 2:

 A = [1, 1, 2, 2, 3]


Example Output

Output 1:

 "WIN"
Output 2:

 "LOSE"


Example Explanation

Explanation 1:

 In the his turn, Tom can take 1 away, and then Harry take take 2 away. The array is empty and both of them have equal number of cards, so we can say that they have won the game.
Explanation 2:

 No matter how they take away the elements, >= 1 card will always remain, hence, they lose.'''

class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        
        '''To win the game, you need two distinct numbers to be present in the array and in equal frequency. In all other cases, the game
           is lost'''
           
        freq = {}
        
        for i in A:
            
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        if len(freq) != 2:
            return "LOSE"
            
        elif len(freq) == 2:
            val = list(freq.values())
            if val[0] == val[1]:
                return "WIN"
            else:
                return "LOSE"

