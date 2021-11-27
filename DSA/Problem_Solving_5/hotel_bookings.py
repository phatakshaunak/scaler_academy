'''Q2. Hotel Bookings Possible
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

A hotel manager has to process N advance bookings of rooms for the next season. His hotel has K rooms.

Bookings contain an arrival date and a departure date.

He wants to find out whether there are enough rooms in the hotel to satisfy the demand.

Write a program that solves this problem in time O(N log N) .



Problem Constraints

1 <= N <= 106

1 <= K <= 106

0 <= arrive[i] <= depart[i] <= 108



Input Format

First argument is an integer array named arrive denoting the arrival times of bookings.

Second argument is an integer array named depart denoting the departure times of bookings.

Third argument is an integer K which denotes count of rooms.



Output Format

A boolean which tells whether its possible to make a booking.

Return 0/1 for C programs.

O -> No there are not enough rooms for N booking.

1 -> Yes there are enough rooms for N booking.



Example Input

Input 1:

 arrive = [1, 3, 5]
 depart = [2, 6, 8]
 K = 1


Example Output

Output 1:

 False / 0 


Example Explanation

Explanation 1:

 At day = 5, there are 2 guests in the hotel. But hotel has only one room so it is not possible to take the booking
 so we will return false or 0 for C Program.'''

class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        
        all = []
        
        for i in range(len(arrive)):
            
            all.append([arrive[i],0])
            all.append([depart[i],1])
        
        all.sort()
        
        counter = 0
        
        for day in all:
            
            if counter > K:
                return 0
            
            elif day[1] == 0:
                counter += 1
            
            else:
                counter -= 1
        
        return 1
        
    
    '''Sorting helps to keep track of earliest arrivals and bookings by adding or subtracting them. Can also be done in a prefix sum array fashion (similar to beggars worshippers approach) although will give TLE/MLE error for 10^8 size array'''