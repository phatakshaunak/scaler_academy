'''Q2. Circle of Monsters
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

You are playing another computer game, and now you have to slay n monsters. These monsters are standing in a circle, numbered clockwise from 1 to n. Initially, the i-th monster has ai health.

You may shoot the monsters to kill them. Each shot requires exactly one bullet and decreases the health of the targeted monster by 1 (deals 1 damage to it). Furthermore, when the health of some monster i becomes 0 or less than 0, it dies and explodes, dealing bi damage to the next monster (monster i+1, if i < n, or monster 1, if i=n). If the next monster is already dead, then nothing happens. If the explosion kills the next monster, it explodes too, damaging the monster after it and possibly triggering another explosion, and so on.

You have to calculate the minimum number of bullets mod 10 9 + 7 you have to fire to kill all n monsters in the circle.

NOTE: If the minimum no. of bullets are x then you have to return x % 1e9 + 7 .



Problem Constraints

2<= n <=300000
1<= A[i], B[i]<= 1e9


Input Format

First Argument is array of integers of N size denoting array A Second Argument is array of integers of N size denoting array B


Output Format

Return the miniumum number of bullets mod 10 9 + 7 you have to fire to kill all of the monsters.


Example Input

Input- 1
A=[7,2,5]
B=[15,14,3]
Input- 2

A=[1 2]
B=[2 1]


Example Output

Output- 1
6
Output- 2

1


Example Explanation

Explanation-1
Firstly we shoot 2nd monster whose health is 2 with 2 bullets and then this monster will create damage of 14 to another monster.
Now 3rd monster health will decrease by 14 units . hence 3rd monster also died . hence it will create damage of 3 units to 1st monster
Now 1st monster health is 7-3=4 . and now 4 more bullets are required to kill 1st monster.
Total bullets required to kill all the monsters = 2+4= 6
Explanation-2

Kill 1st monster with 1 bullet so it will cause 2 units of damage to 2nd monster.
Hence 2nd monster automatically died.
Total bullets required=1'''

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        
        mod = int(1e9+7)
        # Initially calculate sum of all the damage caused to any element from its previous element
        damage = 0
        for i in range(len(A)):
            
            if i == 0:
                damage = damage + max(0, (A[i] - B[len(A) - 1]))
            else:
                damage = damage + max(0, (A[i] - B[i-1]))
        
        # Next iterate over A to find a start point giving minimum bullets
        ans = float("inf")
        for i in range(len(A)):
            
            if i == 0:
                curr = A[i] + damage - max(0, (A[i] - B[len(A) - 1]))
            else:
                curr = A[i] + damage - max(0, (A[i] - B[i-1]))
            
            ans = min(ans, curr)
        
        return ans % mod
            
