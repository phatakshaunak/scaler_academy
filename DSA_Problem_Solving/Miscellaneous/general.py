'''
Amazon OA

Amazon has decided to migrate the inventory data to Amazon.com cloud from other platform. It has the following feature : The cheapest item will be displayed first ,

1st View returns the first cheapest item, similarly kth view returns the kth item in the list so far.
It is ensured that items already exist before the view query;
We have 2 kinds of operations "INSERT", "VIEW". "INSERT" inserts the item into the list, "VIEW" returns the cheapest element ( kth view returns k th cheapest element).

Input : we have each string with 3 entires [ "operation" , "item-name","cost"]
Return: result should be a vector of items when "View" Query comes up;

Eg : [["INSERT", "burger","4"],
["INSERT", "gum","1"],
["VIEW", "-" ,"-" ],
["INSERT", "chocolate","3"],
["INSERT", "PORK", "2"],
["VIEW","-","-"]]
Expected Result : ["GUM","PORK"]

Explanation ->
Gum(1) , burger(4) <-View => return "GUM" ( 1st View //returns first cheapest element from the list so far)
Gum(1), pork(2), chocolate(3), burger(4) => return "PORK" ( 2nd View //returns second cheapest element from the list so far).

I have solved the question using set the following approach, could pass 10/15 TestCases with TLE
TimeComplexity of the algorithm is O(N^2) - since finding the kth element we have to traverse the set from the beginning

vector<string> ShoppingList(vector<vector<string>> entries){
    set<pair<int,string>> s;
    int views = 0;
    vector<string> ans;
    for(auto entry : entries){
        if(entry[0] == "INSERT")
            s.insert(make_pair(stoi(entry[2]),entry[1]));
        else{
            auto it = s.begin();
            advance(it,views);
            ans.push_back(it->second);
            views++;
        }
    }
    return ans;
}
Can anyone suggest any better approach? (Seems like a design problem).

There can be multiple inputs with same prices, in that case we have to return an item with lexographically smaller name.'''

from heapq import heapify, heappush, heappop

class Items:
    
    def __init__(self):
        
        # Max heap at any time maintains a size of k to obtain kth smallest item for kth view in O(1)
        # Min heap maintains excess items that can be added to max heap as needed
        self.minh = []
        self.maxh = []
        self.k = 1
        
    def insert(self, item):
        #Add to max heap, push top to min heap if size exceeds k
        item[0] = item[0] * -1
        heappush(self.maxh, item)
        
        if len(self.maxh) > self.k:
            top = heappop(self.maxh)
            top[0] = top[0] * -1
            heappush(self.minh, top)
        
    def view(self):
        
#         print('before ans', self.maxh)
        ans = self.maxh[0].copy()
        ans[0] = ans[0] * -1
#         print('after ans', self.maxh)
#         print(f"View {self.k}", ans)
        
        self.k += 1
#         print(self.minh, 'min heap', self.maxh)
        
        if self.minh:
            top = heappop(self.minh)
            top[0] = top[0] * -1
#         print(top, 'insert to max heap', self.maxh)
            heappush(self.maxh, top)
        
        return ans
    
# I = Items()
# I.insert([4, 'burger'])
# print(I.maxh, I.minh)
# I.insert([1, 'gum'])

# print(I.view())

# I.insert([3, 'chocolate'])

# I.insert([2, 'pork'])

# I.insert([4, 'beef'])

# print(I.view())

# print(I.view())

I = Items()
I.insert([40, 'burger'])
I.insert([10, 'gum'])
print(I.view())
I.insert([5, 'apple'])
print(I.view())
I.insert([30, 'chocolate'])
I.insert([20, 'pork'])
print(I.view())

I.maxh, I.minh, I.k

'''[10, 'gum']
[10, 'gum']
[20, 'pork']
([[-30, 'chocolate'], [-20, 'pork'], [-10, 'gum'], [-5, 'apple']],
 [[40, 'burger']],
 4)'''

'''

Amazon OA

Question2:
Give you a list servers. Their processing power is given as a array of integer, and boot power as a array of integer.
Write a function to return the max length of sub array which's power consumption is less than or equal to max power limit.
Formula to calculate the power consumption for a subArray is:
Max(bootPower[i...j]) + Sum(processPower[i....j]) * length of subArray.

Note: Single server is also a subArray, return 0 if no such subArray can be found.
'''

from typing import *
from collections import deque
def max_valid_cluster(boot: List[int], process: List[int], limit: int) -> int:
    
    n = len(boot)
    ans = float('-inf')
    
    # To maintain maximum value of boot power in current window
    maxQ = deque()
    
    # Quick access for processing power subarray
    prefix = [0 for i in range(n + 1)]
    
    for i in range(n):
        prefix[i + 1] = prefix[i] + process[i]
    
    left = 0
    
    for right in range(n):
        
        # Deque to maintain window maximum
        while maxQ and boot[maxQ[-1]] <= boot[right]:
            maxQ.pop()
        
        maxQ.append(right)
        
        # Compute the current window power
        curr_power = boot[maxQ[0]] + prefix[right + 1] - prefix[left]
        
        while curr_power > limit:
            
            if left == maxQ[0]:
                print(maxQ)
                maxQ.pop()
            
            left += 1
            print(left, right)
            if left > right:
                break
                
            # Update window power
            curr_power = boot[maxQ[0]] + prefix[right + 1] - prefix[left]
        
        if left <= right:
            
            if ans < right - left + 1:
                print(left, right, curr_power)
                ans = right - left + 1
                
    return ans if ans != float('-inf') else 0

    '''Amazon Academy recently organized a scholarship test on its platform. A total of n students participated in the test. Each student received a unique roll number, i. Each student's rank is stored at rank[i]. Each student gets a unique rank, so rank is a permutation of values 1 through n.

For improved collaboration, the students are to be divided into groups. Use the following rules to find the imbalance of a group of students.

A group has students where 1 <= k <= n.
Groups are formed of students in ranks with consecutive roll numbers, i.e., i, (¡ + 1), .. (1 + K - 1).
The ranks of the students in a group are then sorted ascending to an array, here named sorted_ rank.
The imbalance of the group is then defined as the number of students , who are more than 1 rank beneath the rank of the student just ahead of them, 1.e, sorted rank[i]- sorted rank[i - 1] > 1.
For example, the ranks in a group are [1, 5, 4] so sorted rank = [1, 4, 5).

4-1=3, and 3 > 1. This adds 1 to the imbalance.
5-4=1, and 1 = 1. This does not add to the imbalance.
The imbalance is 1.

Function Description

Givent the ranks of n students, find the total sum of the imbalance of all possible groups.

findTotalImbalance has the following parameter:
int rank[n]: the ranks of each student

Returns

long_int: the total sum of imbalance over all possible groups

Contraints

1 <= n < 3 * 10^3
rank is a permutation of length n
Input0: [4, 1, 3, 2]

Output 0: 3

Explanation 0:
[1] --> [1], imbalance = 0.
[2] --> [2], imbalance = 0.
[3] --> [3], imbalance = 0.
[4] --> [4], imbalance = 0.
[4, 1] --> [1, 4], imbalance = 1.
[1, 3] --> [1, 3], imbalance = 1.
[3, 2] --> [2, 3], imbalance = 0.
[4, 1, 3] --> [1, 3, 4], imbalance = 1.
[1, 3, 2] --> [1, 2, 3], imbalance = 0.
[4, 1, 3, 2] --> [1, 2, 3, 4], imbalance = 0.

Summing it up, the total imbalance is 3,

I did this solution and it didn't pass all of the test (complexity issue).

Can anyone contribute their suggestion how to optimize the solution?'''

################################################################################################################################

'''I found this shipment imbalance variant recently, and had no clue how to solve it:
Given an int array of item weights and integer k, a segment of contiguously placed items can be shipped together if 
and only if the difference between the weights of the heaviest and lightest item differs by at most k to avoid 
load imbalance. find the number of the segment of items can be shipped together
Note: a segment (l,r) is a subarray starts at l and ends at r

Any clue?

Edit:
e.g.:
input: k = 3; weights = [1, 3, 6];
weight difference between max and min for each (l,r) index pair are:

(0,0) -> max(1) - min(1) = 1 - 1 = 0
(0, 1) -> max(1, 3) - min(1, 3) = 3 - 1 = 2
(0, 2) -> max(1, 3, 6) - min(1, 3, 6) = 6- 1 = 5 exceed k = 3
(1, 1) -> max(3) - min(3) = 3- 3 = 0
(1, 2) -> max(3, 6) - min(3, 6) = 6 - 3 = 3
(2, 2) -> max(6) - min(6) = 6 - 6 = 0
5 0f 6 segments have diff <= k, ans is 5

I find this problem from a forum, there is no constraints information in that post, O(N^2) is easy to come up with, I assume the length of the array would be up to 10^5, so approach with O(NLogN) or O(N) would be preferred.

Thank you'''

from collections import deque
def count_groups(arr, limit):
    
    maxQ, minQ = deque(), deque()
    l = 0
    ans = 0
    n = len(arr)
    
    for r in range(n):
        
        while maxQ and arr[maxQ[-1]] <= arr[r]:
            maxQ.pop()
        
        maxQ.append(r)
        
        while minQ and arr[minQ[-1]] >= arr[r]:
            minQ.pop()
        
        minQ.append(r)
        
        while minQ and maxQ and (arr[maxQ[0]] - arr[minQ[0]]) > limit:
            
            if maxQ[0] == l:
                maxQ.popleft()
            
            if minQ[0] == l:
                minQ.popleft()
            
            l += 1
        
        ans += (r - l + 1)
    
    return ans

'''arr = [1, 3, 6]
limit = 3
count_groups(arr, limit)

boot = [1, 2, 3, 4]
process = [1, 2, 3, 4]
limit = 10

max_valid_cluster(boot, process, limit)
'''