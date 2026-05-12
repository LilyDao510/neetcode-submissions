class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # l =len(nums)
        # map ={}
        # for i in range(l):
        #     num = nums[i]
        #     diff = target - num
        #     if diff in map:
        #         return[map[diff],i]
        #     map[num] = i


        l = len(nums)
        map ={}
        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in map:
                return [map[diff],i]
            map[n]= i


