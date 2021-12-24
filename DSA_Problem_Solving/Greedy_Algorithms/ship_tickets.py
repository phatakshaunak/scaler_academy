'''Q3. The ship company
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

The local ship renting service has a special rate plan:

It is up to a passenger to choose a ship.
If the chosen ship has X (X > 0) vacant places at the given moment, then the ticket for such a ship costs X.
The passengers buy tickets in turn, the first person in the queue goes first, then goes the second one, and so on up to A-th person.

You need to tell the maximum and the minimum money that the ship company can earn if all A passengers buy tickets.



Problem Constraints

1 ≤ A ≤ 3000
1 ≤ B ≤ 1000
1 ≤ C[i] ≤ 1000
It is guaranteed that there are at least A empty seats in total.



Input Format

First argument is a integer A denoting the number of passengers in the queue.
Second arugument is a integer B deonting the number of ships.
Third argument is an integer array C of size B where C[i] denotes the number of empty seats in the i-th ship before the ticket office starts selling tickets.



Output Format

Return an array of size 2 denoting the maximum and minimum money that the ship company can earn.



Example Input

Input 1:

 A = 4
 B = 3
 C = [2, 1, 1]
Input 2:

 A = 4
 B = 3
 C = [2, 2, 2]


Example Output

Output 1:

 [5, 5]
Output 2:

[7, 6]


Example Explanation

Explantion 1:

 Maximum money can be earned if the passenger choose : 2(first ship) + 1(first ship) + 1(second ship) + 1(third ship).
 So, the cost will be 5.
 Minimum money can be earned if the passenger choose : 1(senocd ship) + 2(first ship) + 1(first ship) + 1(third ship).
 So, the cost will be 5.
Explanation 2:

 Maximum money can be earned if the passenger choose : 2(first ship) + 2(second ship) + 2(third ship) + 1(first ship).
 So, the cost will be 7.
 Minimum money can be earned if the passenger choose : 2(senocd ship) + 2(first ship) + 1(first ship) + 1(second ship).
 So, the cost will be 6.'''

import heapq
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):

        # Use two heaps, min and max heap
        # Get max val for the number of passengers and add to answer, push remaining tickets back to heap
        # Do the same with the min heap

        t1, t2 = [], []

        t1 = [val for val in C]
        t2 = [(-1 * val) for val in C]

        # min heap
        heapq.heapify(t1)
        # max heap
        heapq.heapify(t2)

        # Max calculation
        m1, ct = 0, A

        while ct > 0:
            top = heapq.heappop(t2) * (-1)
            m1 = m1 + top
            top -= 1
            ct -= 1
            if top > 0:
                heapq.heappush(t2, (-1 * top))
        
        # Min calculation
        m2, ct = 0, A
        
        while ct > 0:
            top = heapq.heappop(t1)
            m2 = m2 + top
            top -= 1
            ct -= 1
            if top > 0:
                heapq.heappush(t1, top)

        return [m1, m2]

        '''
        A = 4
        B = 3
        2, 1, 1

        max heap: 2 1 1
        max_val = 2 + 1 + 1 + 1

        min heap: 1 + 1 + 2
        min_val = 1 + 1 + 2 + 1

        4, 4, [4, 3, 2, 1]
        max: 4 + 3 + 3 + 2 = 12
        min: 1 + 2 + 1 + 3 = 7
        '''