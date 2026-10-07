class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        self.nums = nums

        return (len(nums)*(len(nums)+1))//2-sum(nums)