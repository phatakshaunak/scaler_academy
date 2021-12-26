'''
Q2. Another Coin Problem
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description
The monetary system in DarkLand is really simple and systematic. The locals only use coins. The coins come in different values. The values used are:

 1, 5, 25, 125, 625, 3125, 15625, ...
Formally, for each K >= 0 there are coins worth 5K.

Given an integer A denoting the cost of an item, find and return the smallest number of coins necessary to pay exactly the cost of the item (assuming you have a sufficient supply of coins of each of the types you will need).



Problem Constraints
1 <= A <= 2*109



Input Format
The only argument given is integer A.



Output Format
Return the smallest number of coins necessary to pay exactly the cost of the item.



Example Input
Input 1:

 A = 47
Input 2:

 A = 9


Example Output
Output 1:

 7
Output 2:

 5


Example Explanation
Explanation 1:

 Representation of 7 coins will be : (1 + 1 + 5 + 5 + 5 + 5 + 25).
Explanation 2:

 Representation of 5 coins will be : (1 + 1 + 1 + 1 + 5).
'''
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        # Converting A to base 5 and counting the remainder each time gives the ans
        ans = 0

        while A:
            ans = ans + (A % 5)
            A //= 5
        
        return ans
        # # p = 0
        # pw = 1
        # tmp = A
        # while tmp:
        #     tmp //= 5
        #     if tmp:
        #         pw *= 5
        #         # p += 1
        
        # ans = 0
        # # pw = 5**p
        # while pw:
        #     ans += (A // pw)
        #     A = A % pw
        #     pw //= 5
        
        # return ans