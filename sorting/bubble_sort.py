# idea :Repeatedly swap adjacent elements if they are in wrong order. Largest element bubbles to end 
# complexity
# worst case = O(n^2)
# best case(optimized version) =o(n)

def bubble_sort(l):
  n=len(l)
  for i in range(n):
    for j in range(0, n-i-1):
      if l[j] > l[j+1]
      l[j], l[j+1] = l[j+1], l[j]
  return l
