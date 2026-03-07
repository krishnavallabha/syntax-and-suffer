# useful when:
# sorted list
# size unknow or very large
# main idea :
# 1 → 2 → 4 → 8 → 16
# then binary search
# complexity = O(logn)

def binary_search_range(l, v, low, high):
  while low <= high:
    mid=(low+high)//2
    if l[mid]==v:
      return True
    elif l[mid] < v:
      low= mid +1
    else:
      high=mid -1
  return False


def exponential search(l, v):
if l[0]==v:
  return True
i=1
n=len(l)
while i<n and l[i]<=v:
  i=i*2
return binary_search_range(l, v, i//2, min(i, n-1))
