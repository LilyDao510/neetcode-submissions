class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_nums = set(nums)
        longest = 0

        for i in new_nums:
            if (i-1) not in new_nums:
                length = 1
                while (i+length) in new_nums:
                    length += 1
                longest = max(longest,length)
        return longest
        