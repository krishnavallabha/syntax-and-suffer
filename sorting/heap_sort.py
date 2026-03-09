# # Uses a binary heap data structure.
# Idea:
# Build a max heap
# Remove largest element
# Repeat
# complexity
# building heap = O(n)
# removing elements = O(nlogn)
# total=O(nlogn)

import heapq

def heap_sort(l):
  heapq.heapify(l)
  sorted_list=[]
  while l:
    sorted_list.append(heapq.heappop(l))
  return sorted_list
