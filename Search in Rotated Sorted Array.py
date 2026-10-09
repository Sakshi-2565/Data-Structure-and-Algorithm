###########  Brute Force Solution #################

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)

        for i in range(0,n):
            if nums[i] == target:
                return i
           
        return -1
# Time Complexity = O(N)
# Space Complexity = O(1)

########### OPTIMAL(Binary Search) ##############

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        low,high=0,n-1

        while low<=high:
            mid=(low+high)//2
            if nums[mid] == target:
                return mid
            
            if nums[mid] <= nums[high]:
                if nums[mid]<=target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1

            else:
                if nums[low]<=target<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
        return -1

# Time Complexity = O(logN)
# Space Complexity = O(1)