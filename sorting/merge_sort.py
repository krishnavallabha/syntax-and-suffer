# idea : Divide and Conquer
# 1. split the list in half
# 2. sort both halves
# 3. merge them
# complexity = O(nlogn)

# merge function
def merge (a, b):
  i=0
  j=0
  c=[]
  while i < len(a) and j < len(b):
    if a[i]< b[j]:
      c.append(a[i])
      i+=1
    else:
      c.append(b[j])
      j+=1
  c.extend(a[i:])
  c.extend(b[j:])
  return c

  # merge sort
  def merge_sort(l):
    if len(l) <=1:
      return l
    mid len(l)//2
    left=merge_sort(l[:mid])
    right= merge_sort(l[mid:])
    return merge(left, right)
      
      
