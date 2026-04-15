class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        l, r  = 0, length - 1
        while l < r:
            mid = (l+r)//2
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid +1
        return nums[l]

   
        