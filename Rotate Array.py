class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        self.nums = nums
        self.k = k
        n =len(nums)

        k = k%n
        nums[:] = nums[n-k:] + nums[:n-k]
