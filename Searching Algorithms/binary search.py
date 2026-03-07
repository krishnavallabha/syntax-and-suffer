# complexity=O(logn)
# requirement : Arrays/list elements must be sorted first
# main idea : Always check the middle element

def binarysearch(v,l):
  if l==[]:
    return False
  m=len(l)//2
  if v==l[m]:
    return True
  if v<l[m]:
    return binarysearch(v, l[:m])
  else:
    return binarysearch(v, l[m+1:])

