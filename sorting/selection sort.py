# Idea: Repeatedly find the minimum element and put it in the correct position
# complexity: best = worst = O(n²)
# selection sort always scans full list

def selection_sort(l):
  n=len(l)
  for i in range(n):
    min_pos=i
    for j in range(i+1, n):
      if l[j] < l[min_pos]:
        min_pos=j
    l[i], l[min_pos] = l[min_pos], l[i]
  return l
  
      
