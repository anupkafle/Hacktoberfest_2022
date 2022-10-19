"""
Example:
Input:
N = 8
nums = {1,1,2,2,3,3,3,4}
k = 2
Output: {3, 2}
Explanation: Elements 1 and 2 have the same frequency ie. 2. Therefore, in this
case, the answer includes the element 2 as 2 > 1.
"""
from collections import defaultdict

class Solutions:
    def topK(self, arr, k):  #O(dlogd) where d is frequency of elements and space : O(d)
        d = defaultdict(lambda: 0)
        for i in range(len(arr)):
            d[arr[i]] += 1
        arr.sort(key=lambda x: (d[x], x)) # sorting array based on frequency &&  on value
        ans=[]
        for i in arr[::-1]:
            if i not in ans and k>0:
                ans.append(i)
                k-=1
        return ans
    ###############################################
    def topK(self, arr, k):  #O(klogd+d) where d is frequency of elements and space : O(d); here creating a priority queue of max heap as finding max element in max heap takes log(n) time.
        import heapq

        ans=[]
        d = defaultdict(lambda: 0)
        for i in range(len(arr)):
            d[arr[i]] += 1

        # Using heapq data structure
        heap = [(value, key) for key,
                                 value in d.items()]  #list of pairs (frequency,element). <- priority queue
        # print("heap : ",heap)

        # Get the top k elements
        largest = heapq.nlargest(k, heap)  # O( k log d) taking k largest elements from max heap
        # print("largestK : ",largest)

        # Print the top k elements
        for i in range(k):
            # print(largest[i][1], end =" ")
            ans.append(largest[i][1])

        # print(ans)
        return ans
# [referrence : https://www.geeksforgeeks.org/find-k-numbers-occurrences-given-array/]