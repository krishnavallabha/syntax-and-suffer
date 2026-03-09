# Idea choose a pivot  then divide the list into 
# smaller than pivot 
# pivot
# greater than pivot
# then recursively sort both sides
# complexity
# best/average = O(nlogn)
# worst case: o(n^2) 
# worst happens when list is already sorted

def quick_sort(l):
  if len(l) <=1
  return l
  pivot =l[0]
  left= [x for x in l[1:] if x <= pivot]
  right = [x for x in l[1:] if x>pivot]
  return quick_sort(left) +[pivot] +quick_sort(right
  
