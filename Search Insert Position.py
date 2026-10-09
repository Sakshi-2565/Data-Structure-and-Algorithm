class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        self.nums=nums
        self.target=target
        n=len(nums)
        lb=n
        low=0
        high=n-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]>=target:
                lb=mid
                high = mid-1
            else:
                low = mid+1
        return lb

# Time Complexity = O(logn)
# Space Complexity = O(1)