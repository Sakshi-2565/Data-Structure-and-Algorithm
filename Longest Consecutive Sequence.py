class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        self.nums=nums
        my_set=set(nums)
        longest=0

        for x in my_set:
            if x-1 not in my_set:
                length=0
                while x+length in my_set:
                    length+=1
                longest=max(longest,length)

        return longest

# Time Complexity = O(N+N+N) = O(N) ~ O(N)
# Space Complexity = O(N)