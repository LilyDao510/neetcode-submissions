class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
# Sol 1: Brute force
        l = len(nums)
        res = [1] *l
        for i in range(l):
            prod = 1
            for j in range(l):
                if i == j:
                    continue
                prod *= nums[j]
            res[i] = prod
        return res

            
            

        
        