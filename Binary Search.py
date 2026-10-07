class Solution:
    def search(self, nums: list[int], target: int) -> int:
        self.nums = nums
        self.target = target
        n = len(nums)

        low=0
        high=n-1

        while high>=low:
            mid=(high+low)//2
            if target > nums[mid] :
                low=mid+1
            elif target < nums[mid]:
                high = mid-1
            else:
                return mid

        return -1