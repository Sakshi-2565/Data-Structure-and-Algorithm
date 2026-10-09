############  ITERATITIVE APPROACH  #################
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

# Time Complexity = O(log2n)
# Space Complexity = O(1)

################## RECURSIVE FUNCTION APPROACH #####################

class Solution:
    def search(self,nums,low,high,target):
        self.nums = nums
        self.target = target
        n = len(nums)

        low=0
        high=n-1
        mid = (low+high)//2

        if target == nums[mid] :
            return mid
        elif target > nums[mid]:
            low = mid + 1
            return self.search(nums,low,high,target)
        else:
            high = mid - 1
            return self.search(nums,low,high,target)

# Time Complexity = O(log2n)
# Space Complexity = O(1) 