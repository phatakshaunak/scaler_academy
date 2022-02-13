'''Q4. Merge Intervals
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.



Problem Constraints

0 <= |intervals| <= 105



Input Format

First argument is the vector of intervals

second argument is the new interval to be merged



Output Format

Return the vector of intervals after merging



Example Input

Input 1:

Given intervals [1, 3], [6, 9] insert and merge [2, 5] .
Input 2:

Given intervals [1, 3], [6, 9] insert and merge [2, 6] .


Example Output

Output 1:

 [ [1, 5], [6, 9] ]
Output 2:

 [ [1, 9] ]


Example Explanation

Explanation 1:

(2,5) does not completely merge the given intervals
Explanation 2:

(2,6) completely merges the given intervals'''

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):

        tmp = newInterval
        n = len(intervals)
        ans = []

        for i in range(n):

            # No overlap
            if not(tmp.end >= intervals[i].start and intervals[i].end >= tmp.start):

                if intervals[i].start < tmp.start:
                    ans.append(intervals[i])
                
                else:
                    ans.append(tmp)
                    tmp = intervals[i]
            
            # Overlap (Keep accumulating intervals and insert only when no overlap)
            else:
                tmp.start = min(tmp.start, intervals[i].start)
                tmp.end = max(tmp.end, intervals[i].end)
        
        # Insert the last interval
        ans.append(tmp)

        return ans