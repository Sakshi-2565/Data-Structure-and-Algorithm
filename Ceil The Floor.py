############## OPTIMAL #######################

def getFloorAndCeil(a, n, x):
    floor,ceil=-1,-1
    low,high=0,n-1
    while low<=high:
        mid=(low+high)//2
        if a[mid]==x:
            return [a[mid],a[mid]]

        elif a[mid]<x:
            floor = a[mid]
            low=mid+1
        else:
            ceil=a[mid]
            high = mid-1
            
    return [floor,ceil]

# Time Complexity = O(log2n)
# Space Complexity = O(1)