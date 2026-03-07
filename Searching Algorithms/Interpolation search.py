# Works best when values are uniformly distributed.
# Instead of checking middle, it estimates position.

# complexity 
# best case/average = O(loglogn) !!its not a type its really loglogn
# worst case= O(n)
def interpolation_search(L, v):
    
    low = 0
    high = len(L) - 1
    
    while low <= high and v >= L[low] and v <= L[high]:
        
        if low == high:
            if L[low] == v:
                return True
            return False
        
        pos = low + int(((v - L[low]) * (high - low)) /
                        (L[high] - L[low]))
        
        if L[pos] == v:
            return True
        
        elif L[pos] < v:
            low = pos + 1
        
        else:
            high = pos - 1
            
    return False
