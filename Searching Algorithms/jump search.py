# complexity = O(squareroot(n))
# core Idea= instead of cehcking every element  jump ahead by fixed blocks
# typical block size
# squareroot(n)
# requirement : sorted list
import math
def jumpsearch(v, l):
  n=len(l)
  step=int(math.sqrt(n))
  prev=0
  # jump in blocks
  while prev<n and l[min(step, n)-1]< v:
    prev=step
    step +=int(math.sqrt(n))
    if prev >= n:
      return False
  if prev < min(step, n):
    if l[prev]==v:
      return True
    prev +=1
  return False

      
    
