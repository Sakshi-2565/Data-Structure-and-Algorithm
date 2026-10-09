############# BRUTE FORCE SOLUTION(Linear Search) #############

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        first=-1
        last=-1
        count=0

        for i in range(0,n):
            if nums[i]==target:
                if first == -1:
                    first= i 
                last = i

        return [first,last]

# Time Complexity = O(N)
# Space Complexity = O(1)

##############   OPTIMAL SOLUTION(Binary Search)   ###############

class Solution:
    def LowerBound(self,nums,target):
        n = len(nums)
        low = 0
        high=n-1
        lb=-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]>=target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        return lb

    def UpperBound(self,nums,target):
        n = len(nums)
        low = 0
        high=n-1
        ub=-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]>target:
                ub=mid
                high=mid-1
            else:
                low=mid+1
        return ub

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        LB = self.LowerBound(nums, target)

        if LB == -1 or nums[LB] != target:
            return [-1, -1]

        UB = self.UpperBound(nums, target)

        if UB == -1:
            return [LB, len(nums) - 1]

        return [LB, UB - 1]
            
# Time Complexity = O(2logn) -> O(logn)
# Space Complexity = O(1)