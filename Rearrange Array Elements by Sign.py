class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        self.nums = nums
        n = len(nums)
        result =[0]*n
        pos=0
        neg=1
        for x in nums:
            if x>0:
                result[pos] = x
                pos+=2
            if x<0:
                result[neg] = x
                neg+=2

        return result

# Time Complexity = O(N)
# Space Complexity = O(1)