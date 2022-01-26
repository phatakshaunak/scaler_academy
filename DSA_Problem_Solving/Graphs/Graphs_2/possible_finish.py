'''Q3. Possibility of Finishing
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

There are a total of A courses you have to take, labeled from 1 to A.

Some courses may have prerequisites, for example to take course 2 you have to first take course 1, which is expressed as a pair: [1,2].

So you are given two integer array B and C of same size where for each i (B[i], C[i]) denotes a pair.

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Return 1 if it is possible to finish all the courses, or 0 if it is not possible to finish all the courses.



Problem Constraints

1 <= A <= 6*104

1 <= length(B) = length(C) <= 105

1 <= B[i], C[i] <= A



Input Format

The first argument of input contains an integer A, representing the number of courses.

The second argument of input contains an integer array, B.

The third argument of input contains an integer array, C.



Output Format

Return 1 if it is possible to finish all the courses, or 0 if it is not possible to finish all the courses.



Example Input

Input 1:

 A = 3
 B = [1, 2]
 C = [2, 3]
Input 2:

 A = 2
 B = [1, 2]
 C = [2, 1]


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

 It is possible to complete the courses in the following order:
    1 -> 2 -> 3
Explanation 2:

 It is not possible to complete all the courses.'''

class Solution:
	# @param A : integer
	# @param B : list of integers
	# @param C : list of integers
	# @return an integer
	def solve(self, A, B, C):

        # Do a topological sort using BFS (modified Kahn's algorithm) and if valid, return 1 else 0

        # Stack to store 0 degree nodes
        st = []

        # Build adjacency list and in degree node array
        adj = [[] for i in range(A + 1)]
        in_ = [0 for i in range(A + 1)]

        for i in range(len(B)):

            adj[B[i]].append(C[i])

            in_[C[i]] += 1
        
        # Find non dependent courses, i.e. 0 in degrees
        for i in range(1, len(in_)):

            if in_[i] == 0:
                st.append(i)
        
        # Now loop through all until stack is not empty
        # Keep a count of elements being added to the topological order
        ct = 0

        while st:

            top = st.pop()
            ct += 1
            # Iterate top's adjacency list and decrement their indegrees by 1, append to stack if they become 0
            for nb in adj[top]:

                in_[nb] -= 1

                if in_[nb] == 0:
                    st.append(nb)
        
        # Check if ct is equal to the number of nodes, if yes, then return 1 else 0
        if ct == A:
            return 1
        
        return 0

    # TC: O(V + E), SC: O(V + E)