'''Q5. The Prime Game
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Two players are playing a game. The rules are as follows:

Player 1 always moves first, and both players always play optimally.
Initially there are A piles, where each pile has B number of stones.
The players move in alternating turns. In each turn, a player can choose a pile of size x and reduce the number of stones to y, where 1 <= y < x, and x and y are coprime.
If the current player is unable to make a move, they lose the game.
Determine the winner of the game.


Problem Constraints

1 ≤ A, B ≤ 106



Input Format

The first argument is A, the number of piles. The second argument is B, the number of stones in each pile initially.



Output Format

Return a single integer, 1 or 2, depending upon which player wins.



Example Input

Input 1:

 A = 2
 B = 2
Input 2:

 A = 3
 B = 1


Example Output

Output 1:

 2
Output 2:

 2


Example Explanation

Explanation 1:

 The only possible scenario is player 1 chooses any one pile and reduce it to 1. Then Player 2 reduces the other pile to 1 and wins.
Explanation 2:

 There is no possible move for player 1. Hence, player 2 wins.'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        # Base case, B is 1. In this case, player 1 can't make any moves, thus player 2 wins
        if B == 1:
            return 2
        
        # If A is even, player 2 wins, if A is odd, player 1 wins.
        
        if A % 2 == 0:
            return 2
        
        return 1