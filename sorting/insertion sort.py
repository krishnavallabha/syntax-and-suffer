# Idea : build a sorted list gradually
# similar to sorting playing cards in  our hand
# Complexity
# reverse sorted list =O(n^2)
# best case (already sorted) = O(n)
def insertion_sort(l):
  n=len(l)
  for i in range(n):
    j=i
    while j>0 and l[j] < l[j-1]:
      l[j], l[j-1] = l[j-1], l[j]
      j-=1
  return l
