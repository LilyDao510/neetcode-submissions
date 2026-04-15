class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = len(numbers)
        l, r = 0,i-1
        while l < r:
            res = numbers[l] + numbers[r]
            if res > target:
                r -= 1
            
            elif res < target:
                l += 1
            
            else: 
                return[l+1, r+1]
        return []


         
        