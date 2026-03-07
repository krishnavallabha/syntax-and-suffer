# complexity = O(n)
# Idea: Checks each element sequentially
def linearsearch(v,l):
  for x in l:
    if v==x:
      return True
  return False
  
