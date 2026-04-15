class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Cach 1

        # map= {}
        # for i in nums:
        #     if i in map:
        #         map[i] += 1
        #         if map[i] >1:
        #             return True
        #     else:
        #         map[i] = 1
        # return False

        # Cach 2

        my_set = set()
        for i in nums:
            if i in my_set:
                return True
            else:
                my_set.add(i)
        return False
        
       


            
        