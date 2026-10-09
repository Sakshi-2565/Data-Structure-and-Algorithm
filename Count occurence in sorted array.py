############### BRUTE FORCE SOLUTION (Linear Search)############################

class Solution:
    def countFreq(self, arr, target):
        count = 0
        n = len(arr)
        
        for i in range(0,n):
            if arr[i] == target:
                count+=1
                
            
        return count

# Time Complexity = O(N)
# Space Complexity = O(1)

############# OPTIMAL(Binary Search)##########################

class Solution:
    def LowerBound(self,arr,target):
        n = len(arr)
        low = 0
        high=n-1
        lb=-1
        while low<=high:
            mid = (low+high)//2
            if arr[mid]>=target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        return lb

    def UpperBound(self,arr,target):
        n = len(arr)
        low = 0
        high=n-1
        ub=n
        while low<=high:
            mid = (low+high)//2
            if arr[mid]>target:
                ub=mid
                high=mid-1
            else:
                low=mid+1
        return ub

    def countFreq(self, arr, target):  
        LB = self.LowerBound(arr, target)

        if LB == -1 or arr[LB] != target:
            return 0

        UB = self.UpperBound(arr, target)

        return UB-LB


# Time Complexity = O(2logn) -> O(logn)
# Space Complexity = O(1)
            

